def main():
  user_input = input("Input: ")
  word_without_vowels = shorten(user_input).strip()
  print(word_without_vowels)
 
  



def shorten(word):
  str = ''
  vowels = ['A','a','E','e','I','i','O','o','U','u']
  for char in word:
    if char not in vowels:
      str+=char
  return str

if __name__ == "__main__":
  main()