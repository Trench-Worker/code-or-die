"""pytest tests for letter_grade and answer helpers in quiz_cli."""

from quiz_cli import check_answer, letter_grade, normalize_answer


def test_letter_grade_a():
    assert letter_grade(5, 5) == "A"  # 100%
    assert letter_grade(9, 10) == "A"  # 90%


def test_letter_grade_b():
    assert letter_grade(4, 5) == "B"  # 80%
    assert letter_grade(8, 10) == "B"


def test_letter_grade_c_d_f():
    assert letter_grade(7, 10) == "C"  # 70%
    assert letter_grade(6, 10) == "D"  # 60%
    assert letter_grade(5, 10) == "F"  # 50%
    assert letter_grade(0, 5) == "F"


def test_letter_grade_zero_total():
    assert letter_grade(0, 0) == "F"


def test_normalize_answer():
    assert normalize_answer("  b  ") == "B"
    assert normalize_answer("c") == "C"
    assert normalize_answer("") == ""


def test_check_answer():
    assert check_answer("b", "B") is True
    assert check_answer("A", "B") is False
    assert check_answer("  c ", "C") is True
