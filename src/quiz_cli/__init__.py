"""quiz_cli — code-or-die: a beginner-friendly Python quiz CLI loaded from JSON."""

__version__ = "0.1.0"

from .quiz import check_answer, letter_grade, load_questions, normalize_answer

__all__ = [
    "__version__",
    "check_answer",
    "letter_grade",
    "load_questions",
    "normalize_answer",
]
