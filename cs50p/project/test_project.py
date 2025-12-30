from project import get_sleep_times, get_current_date, get_journal_content

def test_get_sleep_times():
    assert get_sleep_times("5:00 AM") == "5:00 AM"
    assert get_sleep_times("test") == False

def test_get_current_date():
    assert get_current_date("08/16/2023") == "August 16, 2023"
    assert get_current_date("01/01/2000") == "January 01, 2000"

def test_get_journal_content():
    assert get_journal_content("1 1 1 1 1 1 1 1 1 1", 10) == "1 1 1 1 1 1 1 1 1 1"