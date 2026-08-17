#!/usr/bin/env python3

import argparse
import json
import os
import sys
import tempfile
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


SKILL_DIR = Path(__file__).resolve().parents[1]
SCHEMA_PATH = SKILL_DIR / "schemas" / "questionnaire.schema.json"
TEMPLATE_PATH = SKILL_DIR / "assets" / "questionnaire-template.html"
TEMPLATE_MARKER = "__QUESTIONNAIRE_DATA__"


def json_path(parts: list[Any]) -> str:
    path = "$"
    for part in parts:
        if isinstance(part, int):
            path += f"[{part}]"
        else:
            path += f".{part}"
    return path


def load_questionnaire(path: Path) -> dict[str, Any]:
    try:
        with path.open(encoding="utf-8") as input_file:
            value = json.load(input_file)
    except OSError as error:
        raise ValueError(f"{path}: cannot read input: {error.strerror}") from error
    except json.JSONDecodeError as error:
        raise ValueError(
            f"{path}:{error.lineno}:{error.colno}: invalid JSON: {error.msg}"
        ) from error

    if not isinstance(value, dict):
        raise ValueError("$: expected a JSON object")
    return value


def validation_errors(questionnaire: dict[str, Any]) -> list[str]:
    with SCHEMA_PATH.open(encoding="utf-8") as schema_file:
        schema = json.load(schema_file)

    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    errors = [
        f"{json_path(list(error.absolute_path))}: {error.message}"
        for error in sorted(
            validator.iter_errors(questionnaire),
            key=lambda item: tuple(str(part) for part in item.absolute_path),
        )
    ]
    if errors:
        return errors

    seen_section_ids: set[str] = set()
    seen_question_ids: set[str] = set()
    for section_index, section in enumerate(questionnaire["sections"]):
        section_id = section["sectionId"]
        if section_id in seen_section_ids:
            errors.append(
                f'$.sections[{section_index}].sectionId: duplicate section ID "{section_id}"'
            )
        seen_section_ids.add(section_id)

        for question_index, question in enumerate(section["questions"]):
            question_id = question["questionId"]
            question_path = f"$.sections[{section_index}].questions[{question_index}]"
            if question_id in seen_question_ids:
                errors.append(
                    f'{question_path}.questionId: duplicate question ID "{question_id}"'
                )
            seen_question_ids.add(question_id)

            seen_option_ids: set[str] = set()
            for option_index, option in enumerate(question["options"]):
                option_id = option["optionId"]
                if option_id in seen_option_ids:
                    errors.append(
                        f'{question_path}.options[{option_index}].optionId: '
                        f'duplicate option ID "{option_id}"'
                    )
                seen_option_ids.add(option_id)

    return errors


def compile_questionnaire(questionnaire: dict[str, Any], output_path: Path) -> None:
    try:
        template = TEMPLATE_PATH.read_text(encoding="utf-8")
    except OSError as error:
        raise ValueError(f"cannot read questionnaire template: {error}") from error

    marker_count = template.count(TEMPLATE_MARKER)
    if marker_count != 1:
        raise ValueError(
            f"questionnaire template must contain exactly one {TEMPLATE_MARKER} marker; "
            f"found {marker_count}"
        )

    embedded_data = json.dumps(
        questionnaire,
        ensure_ascii=False,
        separators=(",", ":"),
    )
    embedded_data = (
        embedded_data.replace("&", "\\u0026")
        .replace("<", "\\u003c")
        .replace(">", "\\u003e")
    )
    generated_html = template.replace(TEMPLATE_MARKER, embedded_data)

    temporary_path: Path | None = None
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        file_descriptor, temporary_name = tempfile.mkstemp(
            prefix=f".{output_path.name}.",
            dir=output_path.parent,
            text=True,
        )
        temporary_path = Path(temporary_name)
        with os.fdopen(file_descriptor, "w", encoding="utf-8") as output_file:
            output_file.write(generated_html)
        os.replace(temporary_path, output_path)
    except OSError as error:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)
        raise ValueError(f"cannot write output {output_path}: {error}") from error


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate and compile a brainstorm questionnaire."
    )
    parser.add_argument("--validate", action="store_true", help="validate without compiling")
    parser.add_argument("input", type=Path, help="questionnaire JSON input")
    parser.add_argument("output", nargs="?", type=Path, help="standalone HTML output")
    arguments = parser.parse_args()

    if arguments.validate and arguments.output is not None:
        parser.error("output cannot be provided with --validate")
    if not arguments.validate and arguments.output is None:
        parser.error("output is required unless --validate is used")
    return arguments


def main() -> int:
    arguments = parse_arguments()

    try:
        questionnaire = load_questionnaire(arguments.input)
        errors = validation_errors(questionnaire)
    except ValueError as error:
        print(error, file=sys.stderr)
        return 1

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    if arguments.validate:
        print(f"Valid questionnaire: {arguments.input}")
        return 0

    try:
        compile_questionnaire(questionnaire, arguments.output)
    except ValueError as error:
        print(error, file=sys.stderr)
        return 1

    print(f"Compiled questionnaire: {arguments.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
