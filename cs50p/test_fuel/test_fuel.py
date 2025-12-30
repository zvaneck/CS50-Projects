from fuel import convert
from fuel import gauge
import pytest

def test_convert():
    assert convert("3/4") == 75.0

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(75) == "75%"
    assert gauge(99) == "F"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("4/3")
        convert("cat/dog")
