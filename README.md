# code-or-die

[![CI](https://github.com/Trench-Worker/code-or-die/actions/workflows/ci.yml/badge.svg)](https://github.com/Trench-Worker/code-or-die/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![pytest](https://img.shields.io/badge/tests-pytest-green.svg)](tests/)

A polished, beginner-friendly **command-line quiz** written in pure Python.

**code-or-die** loads questions from JSON, scores answers, and prints a letter grade. It showcases practical Python fundamentals: **`argparse`**, **`pathlib`**, **`json`**, and careful **try/except** error handling — plus a non-interactive **`--demo`** mode for CI and screenshots.

The installable package and console script stay `quiz_cli` / `quiz-cli` so `python -m quiz_cli` and `quiz-cli` keep working.

---

## Features

- Load multiple-choice questions from a JSON file
- Interactive mode (type answers at the prompt) or `--demo` (baked answers)
- `--limit N` to run only the first *N* questions
- Letter grades: **A / B / C / D / F** from percent score
- Clear error messages for missing files, bad JSON, and invalid data
- Zero runtime dependencies — just the standard library
- Packaged with `pyproject.toml` and tested with **pytest**
- GitHub Actions CI across Python 3.10–3.13

---

## Requirements

- Python **3.10+**
- `pytest` (optional, for running tests)

---

## Install

```bash
# clone
git clone https://github.com/Trench-Worker/code-or-die.git
cd code-or-die

# optional: virtual environment
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# install package (editable) + dev deps
pip install -e .
pip install -r requirements.txt
```

Without installing, you can still run via `PYTHONPATH`:

```bash
PYTHONPATH=src python -m quiz_cli --demo
```

---

## Usage

```bash
# demo (non-interactive — great for CI / portfolio GIFs)
python -m quiz_cli --demo

# interactive quiz (default questions file)
python -m quiz_cli

# custom questions file
python -m quiz_cli --questions path/to/questions.json

# only the first 3 questions
python -m quiz_cli --demo --limit 3

# after install, the console script also works:
quiz-cli --demo
```

### CLI flags

| Flag | Description |
|------|-------------|
| `--questions PATH` | Path to questions JSON (default: `data/questions.json`) |
| `--demo` | Use baked demo answers (no keyboard needed) |
| `--limit N` | Use only the first *N* questions |

---

## Demo

```text
$ PYTHONPATH=src python -m quiz_cli --demo

(demo mode — using DEMO_ANSWERS)

=== code-or-die ===
Questions: 5

1. Which built-in opens a file for reading?
   A) read()
   B) open()
   C) file()
   D) load()
Your answer: B
  -> Correct!

2. What does json.load(f) do?
   ...
  -> Correct!

...

--- Summary ---
Score: 4/5
Letter grade: B
```

*(Demo intentionally misses one question so the grade lands on **B**.)*

---

## Question format

`data/questions.json` is a JSON **list** of objects:

```json
[
  {
    "id": "q1",
    "prompt": "Which built-in opens a file for reading?",
    "choices": {
      "A": "read()",
      "B": "open()",
      "C": "file()",
      "D": "load()"
    },
    "answer": "B"
  }
]
```

Required keys: `id`, `prompt`, `answer`.  
`choices` is optional (shown when present).

---

## Tests

```bash
pytest -q
```

Coverage focuses on the pure helpers: `letter_grade`, `normalize_answer`, and `check_answer`.

CI also runs a `--demo` smoke test so the CLI stays runnable without a keyboard.

---

## Project layout

```text
code-or-die/
├── README.md
├── LICENSE                 # MIT
├── pyproject.toml          # modern packaging metadata
├── requirements.txt        # pytest for development
├── .gitignore
├── .github/workflows/ci.yml
├── data/
│   └── questions.json
├── src/
│   └── quiz_cli/
│       ├── __init__.py
│       ├── __main__.py     # python -m quiz_cli
│       └── quiz.py         # CLI + grading logic
└── tests/
    └── test_grade.py
```

---

## What this project demonstrates

| Topic | Where |
|-------|--------|
| `argparse` CLI | `quiz.py` → `parse_args` |
| File I/O + `pathlib` | `load_questions` (`Path.read_text`) |
| `json` parsing + validation | `load_questions` |
| Exceptions (`try`/`except`) | `main` |
| Packaging (`src` layout) | `pyproject.toml` |
| Automated tests | `tests/` + GitHub Actions CI |

---

## License

MIT — see [LICENSE](LICENSE).
