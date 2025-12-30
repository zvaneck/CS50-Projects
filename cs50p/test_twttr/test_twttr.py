from twttr import shorten

def test_shorten_lower():
    assert shorten("hello") == "hll"
    assert shorten("vowel") == "vwl"

def test_shorten_upper():
    assert shorten("HELLO") == "HLL"

def test_omit_number():
    assert shorten("hello 123") == "hll 123"

def test_omit_punc():
    assert shorten("hello, world") == "hll, wrld"