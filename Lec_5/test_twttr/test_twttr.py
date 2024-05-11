from twttr import shorten
import pytest

def main():
  test_upper()
  test_upper()
  test_compo()  
  
def test_lower():
  assert shorten('anas') == 'ns'
  assert shorten('aeiou') == ''

def test_upper():
  assert shorten('ANAS') == 'NS'
  assert shorten('AEIOU') == ''

def test_compo():
  assert shorten('Twitter') == 'Twttr'
  assert shorten("What's your name?") == "Wht's yr nm?"
  assert shorten("CS50") == "CS50"
   
  
if __name__ == "__main__":
  main()
  