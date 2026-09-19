# code-or-die

You pick letters. It picks a grade. Survival is a letter, not a vibe.

JSON in. A/B/C/D/F out. Standard library only. No dashboard. No cloud. No feelings.

Python 3.10+. Tests exist. Slide decks do not.

## Install

```bash
git clone https://github.com/Trench-Worker/code-or-die.git
cd code-or-die

python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -e .
pip install -r requirements.txt
```

Or skip the ritual:

```bash
PYTHONPATH=src python -m quiz_cli --demo
```

## Run

```bash
python -m quiz_cli --demo
```

That's the one. No keyboard. Baked answers. Demo misses one on purpose so you get a **B**. Humility ships free.

Type at the prompt if you enjoy consequences:

```bash
python -m quiz_cli
```

Custom file. First N questions. After install, `quiz-cli` also works.

```bash
python -m quiz_cli --questions path/to/questions.json
python -m quiz_cli --demo --limit 3
quiz-cli --demo
```

| Flag | What it does |
|------|----------------|
| `--questions PATH` | JSON list. Default: `data/questions.json` |
| `--demo` | Baked answers. No human required |
| `--limit N` | First N questions. The rest survive |

## Demo

```text
$ python -m quiz_cli --demo

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

...

--- Summary ---
Score: 4/5
Letter grade: B
```

The missing question is not a bug. It is the point.

## Questions

A JSON list. Each object needs `id`, `prompt`, `answer`. `choices` is optional. Show up or stay quiet.

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

Missing file, bad JSON, invalid data: it prints the error. Then it dies. That's the name.

## Tests

```bash
pytest -q
```

Covers the boring parts that matter: `letter_grade`, `normalize_answer`, `check_answer`.

CI (GitHub Actions) runs pytest on Python 3.10–3.13, then:

```bash
python -m quiz_cli --demo --limit 2
```

So the CLI still works when nobody is there to press keys.

## License

MIT. See [LICENSE](LICENSE).
