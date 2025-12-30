import pytest
from seasons import check_birth_date,convert,to_words

def test_check():
    assert check_birth_date("1990-01-01") == True
    with pytest.raises(SystemExit):
        check_birth_date("1990,01,01")

def check_convert():
    assert type(convert("2000-01-01")) == "<class 'datetime.date'>"

def check_words():
    assert to_words(500) == "five hundred minutes"

