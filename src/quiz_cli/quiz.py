"""
code-or-die (quiz_cli) — load quiz questions from JSON, score answers, print a letter grade.

Run:
  PYTHONPATH=src python -m quiz_cli --demo
  # or after install:  quiz-cli --demo
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Package root: .../src/quiz_cli/  →  repo data/ is two levels up from quiz.py's parent
_PACKAGE_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _PACKAGE_DIR.parent.parent
DEFAULT_QUESTIONS = _REPO_ROOT / "data" / "questions.json"

# Baked demo answers: miss q4 on purpose so score is 4/5 -> letter B
DEMO_ANSWERS = {
    "q1": "B",
    "q2": "B",
    "q3": "C",
    "q4": "A",  # wrong on purpose
    "q5": "C",
}


def letter_grade(score: int, total: int) -> str:
    """Return A/B/C/D/F from score out of total."""
    if total <= 0:
        return "F"
    percent = (score / total) * 100
    if percent >= 90:
        return "A"
    if percent >= 80:
        return "B"
    if percent >= 70:
        return "C"
    if percent >= 60:
        return "D"
    return "F"


def normalize_answer(answer: object) -> str:
    """Strip whitespace and uppercase the first character for choice letters."""
    text = str(answer).strip()
    if not text:
        return ""
    return text.upper()[:1]


def check_answer(given: object, expected: object) -> bool:
    """Return True if normalized given matches expected."""
    return normalize_answer(given) == normalize_answer(expected)


def load_questions(path: Path | str) -> list[dict]:
    """
    Load a list of question dicts from a JSON file.

    Uses pathlib for reading. Raises FileNotFoundError / json.JSONDecodeError /
    ValueError on problems.
    """
    path = Path(path)
    text = path.read_text(encoding="utf-8")
    data = json.loads(text)

    if not isinstance(data, list):
        raise ValueError("questions file must contain a JSON list")
    if not data:
        raise ValueError("questions file is empty")

    for i, q in enumerate(data):
        if not isinstance(q, dict):
            raise ValueError(f"question at index {i} must be an object")
        for key in ("id", "prompt", "answer"):
            if key not in q:
                raise ValueError(f"question at index {i} missing '{key}'")

    return data


def format_question(q: dict, number: int) -> str:
    """Build a printable prompt including optional choices."""
    lines = [f"{number}. {q['prompt']}"]
    choices = q.get("choices")
    if isinstance(choices, dict):
        for letter in sorted(choices.keys()):
            lines.append(f"   {letter}) {choices[letter]}")
    lines.append("Your answer: ")
    return "\n".join(lines)


def run_quiz(questions: list[dict], answers_by_id: dict) -> tuple[int, int]:
    """
    Score questions using answers_by_id[qid].

    Print each result and a summary. Return (score, total).
    """
    total = len(questions)
    score = 0

    print("=== code-or-die ===")
    print(f"Questions: {total}\n")

    for i, q in enumerate(questions, start=1):
        print(format_question(q, i), end="")
        given = answers_by_id.get(q["id"], "")
        print(given)

        if check_answer(given, q["answer"]):
            score += 1
            print("  -> Correct!\n")
        else:
            print(f"  -> Incorrect. Expected: {q['answer']}\n")

    grade = letter_grade(score, total)
    print("--- Summary ---")
    print(f"Score: {score}/{total}")
    print(f"Letter grade: {grade}")
    return score, total


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Build CLI with --questions, --demo, and --limit."""
    parser = argparse.ArgumentParser(
        prog="quiz_cli",
        description="code-or-die: a beginner-friendly Python quiz CLI loaded from JSON.",
    )
    parser.add_argument(
        "--questions",
        default=str(DEFAULT_QUESTIONS),
        help=f"Path to questions JSON (default: {DEFAULT_QUESTIONS})",
    )
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Use baked DEMO_ANSWERS (non-interactive)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Only use the first N questions",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    path = Path(args.questions)

    try:
        questions = load_questions(path)
    except FileNotFoundError:
        print(f"Error: questions file not found: {path}", file=sys.stderr)
        return 1
    except json.JSONDecodeError as exc:
        print(f"Error: invalid JSON in {path}: {exc}", file=sys.stderr)
        return 1
    except ValueError as exc:
        print(f"Error: bad questions data: {exc}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"Error: could not read {path}: {exc}", file=sys.stderr)
        return 1

    if args.limit is not None:
        if args.limit < 1:
            print("Error: --limit must be at least 1", file=sys.stderr)
            return 1
        questions = questions[: args.limit]

    if args.demo:
        print("(demo mode — using DEMO_ANSWERS)\n")
        answers = DEMO_ANSWERS
    else:
        # Interactive: ask at the keyboard
        answers = {}
        for i, q in enumerate(questions, start=1):
            print(format_question(q, i), end="")
            answers[q["id"]] = input()
            print()

    run_quiz(questions, answers)
    return 0


def cli() -> None:
    """Console-script entry point (propagates exit code)."""
    raise SystemExit(main())


if __name__ == "__main__":
    cli()
