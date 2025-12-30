from working import convert
import pytest

def test_hour_range():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    with pytest.raises(ValueError):
        convert("13:00 AM to 29:00 PM")


def test_input():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
        convert("cat")

def test_min_range():
    assert convert("9:15 AM to 5:45 PM") == "09:15 to 17:45"
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:90 PM")