from plates import is_valid
import pytest

def test_length():
    assert is_valid('H') == False
    assert is_valid('OUTATIME') == False
    assert is_valid('abcdef') == True

def test_first_char():
    assert is_valid('34AAA') == False
    assert is_valid('CS500') == True
    assert is_valid('123456') == False

def test_numbers():
    assert is_valid('CS05') == False
    assert is_valid('CS50P') == False

def test_punctuation():
    assert is_valid('PI3.14') == False
    assert is_valid('CCCC?') == False
