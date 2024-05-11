from numb3rs import validate
import pytest
import random

def test_case_one():
  assert validate('10.10.10.10.10') == False
def test_case_two():
  assert validate('0.0.0.0') == True
def test_case_three():
  assert validate('255.255.255.255') == True
def test_case_four():
  assert validate('256.256.256.256') == False
  
def test_case_five():
  assert validate('255') == False
def test_case_six():
  assert validate('255.255') == False
def test_case_seven():
  assert validate('1000.256.-5.256') == False
def test_case_eigh():
  assert validate('-1.-1.-1.-1') == False
def test_case_nine():
  assert validate('256.256.256.256') == False
def test_case_ten():
  assert validate('1.256.1.1 ') == False

def test_ip_outside_range():
  assert  validate("256.1.1.1") == False
  assert  validate("1.256.1.1") == False
  assert  validate("1.1.256.1") == False
  assert  validate("1.1.1.256") == False
def test_ip_within_range():
  assert validate("255.1.1.1") == True
  assert validate("1.255.1.1") == True
  assert validate("1.1.255.1") == True
  assert validate("1.1.1.255") == True

def test_ip_in_range():
  ip_iddress = f"{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
  assert validate(ip_iddress) ==  True
  
def test_ip_out_of_range():
  ip_iddress = f"{random.randint(256,1000)}.{random.randint(256,1000)}.{random.randint(256,1000)}.{random.randint(256,1000)}"
  assert validate(ip_iddress) == False
