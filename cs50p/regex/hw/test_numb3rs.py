from numb3rs import validate

def test_range():
    assert validate("1.1.1.1") == True
    assert validate("1.1.1.300") == False

def test_num():
    assert validate("1.1.1.1") == True
    assert validate("1.1.1") == False

def test_alpha_numeric():
    assert validate("1.1.1.1") == True
    assert validate("a.b.c.d") == False