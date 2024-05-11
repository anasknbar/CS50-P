import random
import sys
def main():
  while True:
    try:
      level = int(input("Level: "))
      random_number = random.randint(1,level)
    except ValueError:
      continue
    else:
      game(random_number)
      break
def game(random_number):
  
  while True:
    try:
      user_guess = int(input("Guess: "))
     
    except ValueError:
      continue
    else:
      if user_guess > random_number:
        print("Too large!")
        continue
      elif user_guess < random_number:
        print("Too small!")
        continue
      else:
        sys.exit("Just right!")
        
  
   
main()