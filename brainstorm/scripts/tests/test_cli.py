import copy
import json
import re
import shutil
import socket
import subprocess
import tempfile
import time
import unittest
import urllib.error
import urllib.request
from contextlib import contextmanager
from pathlib import Path


SCRIPTS_DIR = Path(__file__).resolve().parents[1]
COMPILE = SCRIPTS_DIR / "compile"


def valid_questionnaire() -> dict:
    return {
        "questionnaireId": "example-round-1",
        "title": "Example brainstorm",
        "description": "Provide any useful context.",
        "sections": [
            {
                "sectionId": "direction",
                "title": "Direction",
                "description": "Broad decisions about direction.",
                "questions": [
                    {
                        "questionId": "primary-approach",
                        "prompt": "Which approach is most appropriate?",
                        "description": "Choose one, explain it, or leave this unanswered.",
                        "selection": "single",
                        "options": [
                            {
                                "optionId": "approach-alpha",
                                "label": "Approach Alpha",
                                "description": "A short placeholder approach.",
                                "recommended": True,
                            },
                            {
                                "optionId": "approach-beta",
                                "label": "Approach Beta",
                            },
                        ],
                    },
                    {
                        "questionId": "useful-capabilities",
                        "prompt": "Which capabilities are useful?",
                        "selection": "multiple",
                        "options": [
                            {
                                "optionId": "capability-one",
                                "label": "Capability One",
                                "recommended": True,
                            },
                            {
                                "optionId": "capability-two",
                                "label": "Capability Two",
                                "recommended": True,
                            },
                            {
                                "optionId": "capability-three",
                                "label": "Capability Three",
                            },
                        ],
                    },
                ],
            }
        ],
    }


def questionnaire_with_two_sections() -> dict:
    questionnaire = valid_questionnaire()
    questionnaire["sections"].append(
        {
            "sectionId": "constraints",
            "title": "Constraints",
            "description": "Broad constraints for the direction.",
            "questions": [
                {
                    "questionId": "primary-constraint",
                    "prompt": "Which constraint matters most?",
                    "selection": "single",
                    "options": [
                        {
                            "optionId": "simplicity",
                            "label": "Simplicity",
                            "recommended": True,
                        },
                        {
                            "optionId": "flexibility",
                            "label": "Flexibility",
                        },
                    ],
                }
            ],
        }
    )
    return questionnaire


class CompilerCliTests(unittest.TestCase):
    def run_compile(self, *arguments: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [str(COMPILE), *arguments],
            cwd=SCRIPTS_DIR,
            text=True,
            capture_output=True,
            check=False,
        )

    def write_json(self, directory: Path, data: dict) -> Path:
        path = directory / "questionnaire.json"
        path.write_text(json.dumps(data), encoding="utf-8")
        return path

    def webdriver_element(self, base_url: str, session_id: str, selector: str) -> str:
        response = self.webdriver_request(
            base_url,
            "POST",
            f"/session/{session_id}/element",
            {"using": "css selector", "value": selector},
        )
        return response["value"]["element-6066-11e4-a52e-4f735466cecf"]

    def webdriver_request(
        self,
        base_url: str,
        method: str,
        path: str,
        payload: dict | None = None,
    ) -> dict:
        data = None if payload is None else json.dumps(payload).encode("utf-8")
        request = urllib.request.Request(
            f"{base_url}{path}",
            data=data,
            method=method,
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(request, timeout=10) as response:
            return json.load(response)

    def test_user_can_validate_a_well_formed_questionnaire(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            input_path = self.write_json(Path(temporary_directory), valid_questionnaire())

            result = self.run_compile("--validate", str(input_path))

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Valid questionnaire", result.stdout)

    def test_validation_rejects_duplicate_question_ids(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            questionnaire = valid_questionnaire()
            second_section = copy.deepcopy(questionnaire["sections"][0])
            second_section["sectionId"] = "implementation"
            second_section["title"] = "Implementation"
            questionnaire["sections"].append(second_section)
            input_path = self.write_json(Path(temporary_directory), questionnaire)

            result = self.run_compile("--validate", str(input_path))

            self.assertEqual(result.returncode, 1)
            self.assertIn(
                '$.sections[1].questions[0].questionId: duplicate question ID "primary-approach"',
                result.stderr,
            )

    def test_validation_rejects_duplicate_section_and_option_ids(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            questionnaire = valid_questionnaire()
            duplicate_section = copy.deepcopy(questionnaire["sections"][0])
            duplicate_section["questions"] = [
                {
                    "questionId": "another-question",
                    "prompt": "Another question?",
                    "selection": "single",
                    "options": [
                        {
                            "optionId": "same-option",
                            "label": "First label",
                            "recommended": True,
                        },
                        {
                            "optionId": "same-option",
                            "label": "Second label",
                        },
                    ],
                }
            ]
            questionnaire["sections"].append(duplicate_section)
            input_path = self.write_json(Path(temporary_directory), questionnaire)

            result = self.run_compile("--validate", str(input_path))

            self.assertEqual(result.returncode, 1)
            self.assertIn(
                '$.sections[1].sectionId: duplicate section ID "direction"',
                result.stderr,
            )
            self.assertIn(
                '$.sections[1].questions[0].options[1].optionId: duplicate option ID "same-option"',
                result.stderr,
            )

    def test_user_can_compile_a_standalone_questionnaire(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            directory = Path(temporary_directory)
            questionnaire = valid_questionnaire()
            input_path = self.write_json(directory, questionnaire)
            output_path = directory / "questionnaire.html"

            result = self.run_compile(str(input_path), str(output_path))

            self.assertEqual(result.returncode, 0, result.stderr)
            generated_html = output_path.read_text(encoding="utf-8")
            self.assertTrue(generated_html.startswith("<!doctype html>"))
            embedded_data = re.search(
                r'<script id="questionnaire-data" type="application/json">(.*?)</script>',
                generated_html,
                re.DOTALL,
            )
            self.assertIsNotNone(embedded_data)
            self.assertEqual(json.loads(embedded_data.group(1)), questionnaire)

    def test_embedded_questionnaire_text_cannot_break_out_of_data_script(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            directory = Path(temporary_directory)
            questionnaire = valid_questionnaire()
            questionnaire["title"] = '</script><script id="injected">alert(1)</script>'
            input_path = self.write_json(directory, questionnaire)
            output_path = directory / "questionnaire.html"

            result = self.run_compile(str(input_path), str(output_path))

            self.assertEqual(result.returncode, 0, result.stderr)
            generated_html = output_path.read_text(encoding="utf-8")
            self.assertNotIn('<script id="injected">', generated_html)
            self.assertIn("\\u003c/script\\u003e", generated_html)

    def test_invalid_input_does_not_produce_html(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            directory = Path(temporary_directory)
            questionnaire = valid_questionnaire()
            questionnaire["sections"][0]["questions"][0]["dependsOn"] = "another-answer"
            input_path = self.write_json(directory, questionnaire)
            output_path = directory / "questionnaire.html"

            result = self.run_compile(str(input_path), str(output_path))

            self.assertEqual(result.returncode, 1)
            self.assertIn("Additional properties are not allowed", result.stderr)
            self.assertIn("dependsOn", result.stderr)
            self.assertFalse(output_path.exists())

    def test_single_choice_requires_exactly_one_recommendation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            directory = Path(temporary_directory)
            questionnaire = valid_questionnaire()
            questionnaire["sections"][0]["questions"][0]["options"][1][
                "recommended"
            ] = True
            input_path = self.write_json(directory, questionnaire)

            result = self.run_compile("--validate", str(input_path))

            self.assertEqual(result.returncode, 1)
            self.assertIn("$.sections[0].questions[0].options", result.stderr)

    @contextmanager
    def browser_session(self, output_path: Path, download_directory: Path):
        chromedriver = shutil.which("chromedriver")
        if chromedriver is None:
            self.skipTest("chromedriver is not installed")

        with socket.socket() as available_port:
            available_port.bind(("127.0.0.1", 0))
            port = available_port.getsockname()[1]

        driver = subprocess.Popen(
            [chromedriver, f"--port={port}"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        base_url = f"http://127.0.0.1:{port}"
        session_id = None
        try:
            for _ in range(100):
                try:
                    self.webdriver_request(base_url, "GET", "/status")
                    break
                except (urllib.error.URLError, TimeoutError):
                    time.sleep(0.05)
            else:
                self.fail("chromedriver did not become ready")

            session = self.webdriver_request(
                base_url,
                "POST",
                "/session",
                {
                    "capabilities": {
                        "alwaysMatch": {
                            "browserName": "chrome",
                            "goog:chromeOptions": {
                                "args": ["--headless=new", "--no-sandbox", "--disable-gpu"],
                                "prefs": {
                                    "download.default_directory": str(download_directory),
                                    "download.prompt_for_download": False,
                                    "profile.default_content_setting_values.clipboard": 1,
                                },
                            },
                        }
                    }
                },
            )
            session_id = session["value"]["sessionId"]
            self.webdriver_request(
                base_url,
                "POST",
                f"/session/{session_id}/url",
                {"url": output_path.as_uri()},
            )
            yield base_url, session_id
        finally:
            if session_id is not None:
                try:
                    self.webdriver_request(
                        base_url,
                        "DELETE",
                        f"/session/{session_id}",
                    )
                except (urllib.error.URLError, TimeoutError):
                    pass
            driver.terminate()
            driver.wait(timeout=10)

    def browser_script(self, base_url: str, session_id: str, script: str):
        return self.webdriver_request(
            base_url,
            "POST",
            f"/session/{session_id}/execute/sync",
            {"script": script, "args": []},
        )["value"]

    def browser_async_script(self, base_url: str, session_id: str, script: str):
        return self.webdriver_request(
            base_url,
            "POST",
            f"/session/{session_id}/execute/async",
            {"script": script, "args": []},
        )["value"]

    def test_user_can_copy_the_answer_filename(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            directory = Path(temporary_directory)
            input_path = self.write_json(directory, valid_questionnaire())
            output_path = directory / "questionnaire.html"
            result = self.run_compile(str(input_path), str(output_path))
            self.assertEqual(result.returncode, 0, result.stderr)

            with self.browser_session(output_path, directory) as (base_url, session_id):
                copy_button = self.webdriver_element(
                    base_url,
                    session_id,
                    "#copy-filename-button",
                )
                self.webdriver_request(
                    base_url,
                    "POST",
                    f"/session/{session_id}/element/{copy_button}/click",
                    {},
                )
                copied_text = self.browser_async_script(
                    base_url,
                    session_id,
                    """
                    const done = arguments[arguments.length - 1];
                    navigator.clipboard.readText().then(done, (error) => {
                      done(`clipboard error: ${error.name}`);
                    });
                    """,
                )
                status_text = self.browser_script(
                    base_url,
                    session_id,
                    "return document.getElementById('status').textContent;",
                )

                self.assertEqual(copied_text, "example-round-1-answers.json")
                self.assertEqual(
                    status_text,
                    'Answer filename copied: "example-round-1-answers.json".',
                )

    def test_user_can_switch_theme_and_the_choice_persists(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            directory = Path(temporary_directory)
            input_path = self.write_json(directory, valid_questionnaire())
            output_path = directory / "questionnaire.html"
            result = self.run_compile(str(input_path), str(output_path))
            self.assertEqual(result.returncode, 0, result.stderr)

            with self.browser_session(output_path, directory) as (base_url, session_id):
                initial_theme = self.browser_script(
                    base_url,
                    session_id,
                    "return document.documentElement.dataset.theme;",
                )
                self.assertIn(initial_theme, {"light", "dark"})

                toggle = self.webdriver_element(base_url, session_id, "#theme-toggle")
                self.webdriver_request(
                    base_url,
                    "POST",
                    f"/session/{session_id}/element/{toggle}/click",
                    {},
                )
                selected_theme = self.browser_script(
                    base_url,
                    session_id,
                    "return document.documentElement.dataset.theme;",
                )
                self.assertEqual(
                    selected_theme,
                    "light" if initial_theme == "dark" else "dark",
                )

                self.webdriver_request(
                    base_url,
                    "POST",
                    f"/session/{session_id}/url",
                    {"url": output_path.as_uri()},
                )
                restored_theme = self.browser_script(
                    base_url,
                    session_id,
                    "return document.documentElement.dataset.theme;",
                )
                self.assertEqual(restored_theme, selected_theme)

    def test_user_can_navigate_section_tabs_and_the_active_tab_persists(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            directory = Path(temporary_directory)
            input_path = self.write_json(directory, questionnaire_with_two_sections())
            output_path = directory / "questionnaire.html"
            result = self.run_compile(str(input_path), str(output_path))
            self.assertEqual(result.returncode, 0, result.stderr)

            with self.browser_session(output_path, directory) as (base_url, session_id):
                initial_state = self.browser_script(
                    base_url,
                    session_id,
                    """
                    return {
                      tabs: Array.from(document.querySelectorAll('[role="tab"]')).map(
                        (tab) => ({
                          text: tab.textContent.trim(),
                          selected: tab.getAttribute('aria-selected')
                        })
                      ),
                      panels: Array.from(document.querySelectorAll('[role="tabpanel"]')).map(
                        (panel) => ({id: panel.id, hidden: panel.hidden})
                      )
                    };
                    """,
                )
                self.assertEqual(
                    initial_state,
                    {
                        "tabs": [
                            {"text": "Direction", "selected": "true"},
                            {"text": "Constraints", "selected": "false"},
                        ],
                        "panels": [
                            {"id": "section-direction", "hidden": False},
                            {"id": "section-constraints", "hidden": True},
                        ],
                    },
                )

                direction_tab = self.webdriver_element(
                    base_url,
                    session_id,
                    "#tab-direction",
                )
                self.webdriver_request(
                    base_url,
                    "POST",
                    f"/session/{session_id}/element/{direction_tab}/value",
                    {"text": "\ue014", "value": ["\ue014"]},
                )
                selected_tab = self.browser_script(
                    base_url,
                    session_id,
                    "return document.querySelector('[role=tab][aria-selected=true]').id;",
                )
                self.assertEqual(selected_tab, "tab-constraints")

                self.webdriver_request(
                    base_url,
                    "POST",
                    f"/session/{session_id}/url",
                    {"url": output_path.as_uri()},
                )
                restored_tab = self.browser_script(
                    base_url,
                    session_id,
                    "return document.querySelector('[role=tab][aria-selected=true]').id;",
                )
                self.assertEqual(restored_tab, "tab-constraints")

    def test_previous_and_next_navigation_return_viewport_to_page_top(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            directory = Path(temporary_directory)
            input_path = self.write_json(directory, questionnaire_with_two_sections())
            output_path = directory / "questionnaire.html"
            result = self.run_compile(str(input_path), str(output_path))
            self.assertEqual(result.returncode, 0, result.stderr)

            with self.browser_session(output_path, directory) as (base_url, session_id):
                self.browser_script(
                    base_url,
                    session_id,
                    "window.scrollTo(0, document.body.scrollHeight); return window.scrollY;",
                )
                next_button = self.webdriver_element(
                    base_url,
                    session_id,
                    ".next-section",
                )
                self.webdriver_request(
                    base_url,
                    "POST",
                    f"/session/{session_id}/element/{next_button}/click",
                    {},
                )
                next_state = self.browser_script(
                    base_url,
                    session_id,
                    """
                    return {
                      activeTab: document.querySelector('[role=tab][aria-selected=true]').id,
                      scrollY: window.scrollY
                    };
                    """,
                )
                self.assertEqual(
                    next_state,
                    {"activeTab": "tab-constraints", "scrollY": 0},
                )

                self.browser_script(
                    base_url,
                    session_id,
                    "window.scrollTo(0, document.body.scrollHeight); return window.scrollY;",
                )
                previous_button = self.webdriver_element(
                    base_url,
                    session_id,
                    ".section-navigation button:not(.next-section)",
                )
                self.webdriver_request(
                    base_url,
                    "POST",
                    f"/session/{session_id}/element/{previous_button}/click",
                    {},
                )
                previous_state = self.browser_script(
                    base_url,
                    session_id,
                    """
                    return {
                      activeTab: document.querySelector('[role=tab][aria-selected=true]').id,
                      scrollY: window.scrollY
                    };
                    """,
                )
                self.assertEqual(
                    previous_state,
                    {"activeTab": "tab-direction", "scrollY": 0},
                )

    def test_questions_and_tabs_show_when_context_has_been_added(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            directory = Path(temporary_directory)
            input_path = self.write_json(directory, questionnaire_with_two_sections())
            output_path = directory / "questionnaire.html"
            result = self.run_compile(str(input_path), str(output_path))
            self.assertEqual(result.returncode, 0, result.stderr)

            with self.browser_session(output_path, directory) as (base_url, session_id):
                initial_state = self.browser_script(
                    base_url,
                    session_id,
                    """
                    const question = document.getElementById('question-primary-approach');
                    const badge = document.querySelector('#tab-direction .tab-response-count');
                    return {
                      questionHasResponse: question.classList.contains('has-response'),
                      badgeHidden: badge.hidden,
                      badgeText: badge.textContent
                    };
                    """,
                )
                self.assertEqual(
                    initial_state,
                    {
                        "questionHasResponse": False,
                        "badgeHidden": True,
                        "badgeText": "",
                    },
                )

                radio = self.webdriver_element(
                    base_url,
                    session_id,
                    '#question-primary-approach input[value="approach-alpha"]',
                )
                self.webdriver_request(
                    base_url,
                    "POST",
                    f"/session/{session_id}/element/{radio}/click",
                    {},
                )
                selected_state = self.browser_script(
                    base_url,
                    session_id,
                    """
                    return {
                      questionHasResponse: document.getElementById('question-primary-approach')
                        .classList.contains('has-response'),
                      badgeText: document.querySelector(
                        '#tab-direction .tab-response-count'
                      ).textContent
                    };
                    """,
                )
                self.assertEqual(
                    selected_state,
                    {"questionHasResponse": True, "badgeText": "1"},
                )

                self.webdriver_request(
                    base_url,
                    "POST",
                    f"/session/{session_id}/element/{radio}/click",
                    {},
                )
                cleared_state = self.browser_script(
                    base_url,
                    session_id,
                    """
                    return document.getElementById('question-primary-approach')
                      .classList.contains('has-response');
                    """,
                )
                self.assertFalse(cleared_state)

                question_text = self.webdriver_element(
                    base_url,
                    session_id,
                    "#question-primary-approach .question-text",
                )
                self.webdriver_request(
                    base_url,
                    "POST",
                    f"/session/{session_id}/element/{question_text}/value",
                    {"text": "Useful context", "value": list("Useful context")},
                )
                answered_state = self.browser_script(
                    base_url,
                    session_id,
                    """
                    const question = document.getElementById('question-primary-approach');
                    const badge = document.querySelector('#tab-direction .tab-response-count');
                    return {
                      questionHasResponse: question.classList.contains('has-response'),
                      contextBadgeVisible: !question.querySelector('.response-badge').hidden,
                      tabHasResponse: document.getElementById('tab-direction')
                        .classList.contains('has-response'),
                      badgeHidden: badge.hidden,
                      badgeText: badge.textContent
                    };
                    """,
                )
                self.assertEqual(
                    answered_state,
                    {
                        "questionHasResponse": True,
                        "contextBadgeVisible": True,
                        "tabHasResponse": True,
                        "badgeHidden": False,
                        "badgeText": "1",
                    },
                )

                self.webdriver_request(
                    base_url,
                    "POST",
                    f"/session/{session_id}/url",
                    {"url": output_path.as_uri()},
                )
                restored_state = self.browser_script(
                    base_url,
                    session_id,
                    """
                    return {
                      questionHasResponse: document.getElementById('question-primary-approach')
                        .classList.contains('has-response'),
                      badgeText: document.querySelector(
                        '#tab-direction .tab-response-count'
                      ).textContent
                    };
                    """,
                )
                self.assertEqual(
                    restored_state,
                    {"questionHasResponse": True, "badgeText": "1"},
                )

    def test_generated_page_collects_independently_understandable_answers(self) -> None:
        chromedriver = shutil.which("chromedriver")
        if chromedriver is None:
            self.skipTest("chromedriver is not installed")

        with tempfile.TemporaryDirectory() as temporary_directory:
            directory = Path(temporary_directory)
            questionnaire = valid_questionnaire()
            input_path = self.write_json(directory, questionnaire)
            output_path = directory / "questionnaire.html"
            result = self.run_compile(str(input_path), str(output_path))
            self.assertEqual(result.returncode, 0, result.stderr)

            with socket.socket() as available_port:
                available_port.bind(("127.0.0.1", 0))
                port = available_port.getsockname()[1]

            driver = subprocess.Popen(
                [chromedriver, f"--port={port}"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            base_url = f"http://127.0.0.1:{port}"
            session_id = None
            try:
                for _ in range(100):
                    try:
                        self.webdriver_request(base_url, "GET", "/status")
                        break
                    except (urllib.error.URLError, TimeoutError):
                        time.sleep(0.05)
                else:
                    self.fail("chromedriver did not become ready")

                session = self.webdriver_request(
                    base_url,
                    "POST",
                    "/session",
                    {
                        "capabilities": {
                            "alwaysMatch": {
                                "browserName": "chrome",
                                "goog:chromeOptions": {
                                    "args": ["--headless=new", "--no-sandbox", "--disable-gpu"],
                                    "prefs": {
                                        "download.default_directory": str(directory),
                                        "download.prompt_for_download": False
                                    }
                                },
                            }
                        }
                    },
                )
                session_id = session["value"]["sessionId"]
                self.webdriver_request(
                    base_url,
                    "POST",
                    f"/session/{session_id}/url",
                    {"url": output_path.as_uri()},
                )
                radio = self.webdriver_element(
                    base_url,
                    session_id,
                    '#question-primary-approach input[value="approach-alpha"]',
                )
                self.webdriver_request(
                    base_url,
                    "POST",
                    f"/session/{session_id}/element/{radio}/click",
                    {},
                )
                question_text = self.webdriver_element(
                    base_url,
                    session_id,
                    "#question-primary-approach .question-text",
                )
                self.webdriver_request(
                    base_url,
                    "POST",
                    f"/session/{session_id}/element/{question_text}/value",
                    {"text": "Written context", "value": list("Written context")},
                )
                section_comment = self.webdriver_element(
                    base_url,
                    session_id,
                    "#comment-direction",
                )
                self.webdriver_request(
                    base_url,
                    "POST",
                    f"/session/{session_id}/element/{section_comment}/value",
                    {"text": "Section context", "value": list("Section context")},
                )
                download_button = self.webdriver_element(
                    base_url,
                    session_id,
                    "#download-button",
                )
                self.webdriver_request(
                    base_url,
                    "POST",
                    f"/session/{session_id}/element/{download_button}/click",
                    {},
                )

                answer_path = directory / "example-round-1-answers.json"
                for _ in range(100):
                    if answer_path.exists():
                        break
                    time.sleep(0.05)
                else:
                    self.fail("answer download was not created")
                answer_result = json.loads(answer_path.read_text(encoding="utf-8"))

                self.assertEqual(answer_result["questionnaireId"], "example-round-1")
                self.assertEqual(answer_result["title"], "Example brainstorm")
                self.assertEqual(answer_result["sections"][0]["title"], "Direction")
                self.assertEqual(answer_result["sections"][0]["comment"], "Section context")
                first_answer = answer_result["sections"][0]["answers"][0]
                self.assertEqual(first_answer["prompt"], "Which approach is most appropriate?")
                self.assertEqual(
                    first_answer["selectedOptions"],
                    [{"optionId": "approach-alpha", "label": "Approach Alpha"}],
                )
                self.assertEqual(first_answer["textAnswer"], "Written context")
                self.assertEqual(
                    answer_result["sections"][0]["answers"][1]["selectedOptions"],
                    [],
                )

                self.webdriver_request(
                    base_url,
                    "POST",
                    f"/session/{session_id}/element/{radio}/click",
                    {},
                )
                selected_state = self.webdriver_request(
                    base_url,
                    "GET",
                    f"/session/{session_id}/element/{radio}/selected",
                )["value"]
                self.assertFalse(selected_state)
            finally:
                if session_id is not None:
                    try:
                        self.webdriver_request(
                            base_url,
                            "DELETE",
                            f"/session/{session_id}",
                        )
                    except (urllib.error.URLError, TimeoutError):
                        pass
                driver.terminate()
                driver.wait(timeout=10)


if __name__ == "__main__":
    unittest.main()
