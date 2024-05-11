from fuel import convert 
from fuel import gauge
import pytest

def main():
  ...
  
def test_f():
  assert convert('99/100') == 99
  assert gauge(99) == 'F'
  assert convert('1/1') == 100
  assert gauge(100) == 'F'
  
def test_e():
  assert convert('1/100') == 1
  assert gauge(1) == 'E'
  assert convert('0/1') == 0
  assert gauge(0) == 'E'
  
def test_btween():
  assert convert('50/100') == 50
  assert gauge(50) == '50%'
  assert convert('3/4') == 75
  assert gauge(75) == '75%'
  
def test_convert_with_invalid_input():
  with pytest.raises(ValueError):
      convert('e/6')
  with pytest.raises(ZeroDivisionError):
      convert('4/0')
      
  
if __name__ == "__main__":
    main()