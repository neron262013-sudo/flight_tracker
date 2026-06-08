from src.utils import normalize_value


def test_normalize_value_none():
    assert normalize_value(None) == 0


def test_normalize_value_negative():
    assert normalize_value(-10) == 0


def test_normalize_value_positive():
    assert normalize_value(50) == 50
