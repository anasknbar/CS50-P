from project import add,multiply,divide
import pytest

def test_add():
    assert add(1+100) == 101
    assert add(1+70) == 71


def test_multiply():
    assert multiply(0,100000) == 0
    assert multiply(10,10) == 100


def test_divide():
    assert divide(100,10) == 10
    assert divide(100,1) == 100



