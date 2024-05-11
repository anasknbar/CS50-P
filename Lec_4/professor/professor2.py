import random


def main():
    level = get_level()
    score = 0
    while True:
      for _ in range(1,11):
          num_1, num_2, answer = generate_integer(level)
          try:
            user_answer = int(input(f"{num_1} + {num_2} = ")) 
            if not(user_answer == answer):
              raise ValueError
            else:
              score +=1
          except ValueError:
            print("EEE")
            for chance in range(2):
              try:
                user_answer = int(input(f"{num_1} + {num_2} = ")) 
                if user_answer == answer:
                  score += 1
                  break
                else:
                  raise ValueError
              except ValueError:
                  print("EEE")
                  continue
            if not (user_answer == answer):
              print(f"{num_1} + {num_2} = {answer}") 
      print(f"Score: {score}")
      break


def get_level():
    while True:
      try:
        level = int(input("Level: "))
        if level not in [1,2,3]:
          raise ValueError
      except ValueError:
        continue
      else:
        return level
        
            
        
      


def generate_integer(level):
    if level == 1:
      num_1 = random.randint(0,9)
      num_2 = random.randint(0,9)
      answer = num_1 + num_2
      return [num_1,num_2,answer]
    elif level == 2:
      num_1 = random.randint(10,99)
      num_2 = random.randint(10,99)
      answer = num_1 + num_2
      return [num_1,num_2,answer]
      
    elif level == 3:
      num_1 = random.randint(100,999)
      num_2 = random.randint(100,999)
      answer = num_1 + num_2
      return [num_1,num_2,answer]
      


if __name__ == "__main__":
    main()
