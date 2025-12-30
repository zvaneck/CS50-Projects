from um import count

def test_case():
    assert count("UM, hello, UM") == 2
    assert count("um, hello, Um") == 2

def test_substring():
    assert count("yum") == 0
    assert count("um, yummy") == 1

def test_punct():
    assert count("um.um:um") == 3
    assert count(".um.   um. um?") == 3