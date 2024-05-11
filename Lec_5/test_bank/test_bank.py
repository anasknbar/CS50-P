from plates import is_valid
import pytest

def test_length():
    assert is_valid('w') == False
    assert is_valid('we') == True

def test_first_char():
    assert is_valid('34AAA') == False
    assert is_valid('C350') == False

def test_numbers():
    assert is_valid('AAA222') == True
    assert is_valid('AAA0222') == False

def test_punctuation():
    assert is_valid('BB12.6') == False
    assert is_valid('CCCC?') == False
