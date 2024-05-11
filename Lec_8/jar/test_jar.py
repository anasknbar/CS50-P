from my_jar import Jar
import pytest

def test_init():
  jar = Jar()
  assert jar.capacity == 12

def test_str():
  jar = Jar()
  jar.deposit(10)
  assert jar.size == 10
  
def test_deposit():
  jar = Jar()
  jar.deposit(10)
  assert jar.size == 10
  
  with pytest.raises(ValueError):
    jar.deposit(13)
    
def test_withdraw():
  jar = Jar()
  jar.deposit(10)
  jar.withdraw(5)
  assert jar.size == 5