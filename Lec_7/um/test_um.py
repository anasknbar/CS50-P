from um import count
import py

def test_single_um():
  assert count('um') == 1
  assert count('um?') == 1
  assert count('um,') == 1
  assert count('uM') == 1
  assert count('Um?') == 1
  assert count('UM?') == 1
  assert count('Um, thanks for the album.') == 1
  
def test_multiple_um():
  assert count('Um, thanks, um...') == 2
  assert count('Um um UUm um, umk umum') == 3