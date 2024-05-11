from seasons import converter
import pytest


def test_date():
  assert converter('2003-5-17') == 11026080
  assert converter('2000-2-1') == 12755520
  assert converter('1991-1-1') == 17533440
def test_invalid_date():
  with pytest.raises(ValueError):
    converter('29-1-2983')

 