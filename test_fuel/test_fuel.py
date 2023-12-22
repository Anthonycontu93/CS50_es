import pytest
from fuel import convert
from fuel import gauge


def test_convert_str():
    """Convert a string to a X/Y fraction with its numerator and denominator represented
    by an integer between 0 and 100, inclusive."""

    assert convert("1/1") == 100
    assert convert("1/2") == 50
    assert convert("1/50") == 2
    assert convert("0/8") == 0

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_value_error():
    with pytest.raises(ValueError):
        convert("2/1")

def test_gauge():
    """Give integer between 1 and 99, gauge should return value. If below 1 percent or above 99%, display 'E' or 'F', respectively."""
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(98) == "98%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"