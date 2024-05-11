def main():
  user_input = input("Input: ")
  str_without_vowels = vowels_omitter(user_input)
  print(str_without_vowels)
 
  



def vowels_omitter(s):
  str = ''
  vowels = ['A','a','E','e','I','i','O','o','U','u']
  for char in s:
    if char not in vowels:
      str+=char
  return str


main()