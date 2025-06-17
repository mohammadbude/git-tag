
from extreactdigit import extract_digits

def test_single_match():
    assert extract_digits("There are 42 apples") == ["42"]

def test_multiple_matches():
    assert extract_digits("Dates: 2023, 06, 16") == ["2023", "06", "16"]

def test_no_digits():
    assert extract_digits("No numbers here!") == []

def test_with_letters():
    assert extract_digits("abc123 def456") != ["123", "456"]

