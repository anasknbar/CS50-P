import string
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if length(s) and first_two_char(s) and no_punctuation_and_space(s) and no_number_in_the_middle(s):
      return True 

def length(s):
  return  2 <= len(s) <= 6 
def first_two_char(s):
   return s[0:2].isalpha()
def no_punctuation_and_space(s):
  return  (not any(x in string.punctuation for x in s)) and ' ' not in s


def no_number_in_the_middle(s):
  string = ''
  for index,char in enumerate(s) :
    if char.isdigit():
      string = (s[index:])
      break
    else:
      continue
  if len(string) > 0:
    if string.isdigit() and string[0] != '0':
      return True
    else:
      return False
  else:
    return True
main()


# s = 'ab4'
# print(s.isalpha()) >> false
