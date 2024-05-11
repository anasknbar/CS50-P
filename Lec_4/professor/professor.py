import random
import sys

def main():
  while True:
    try:
      level = int(input("Level: "))
      if  level <= 0 or level > 3:
        raise ValueError
    except ValueError:
      continue
    else:
      get_level(level)
      sys.exit()
    
def get_level(level):
  score = 0
  for math_problem in range(1,11):
    num_1,num_2,correct_answer = generate_integer(level)
    
    try:
      user_answer = int(input(f"{num_1} + {num_2} = "))
      if not(user_answer == correct_answer ):
        print("EEE")
        for chance in range(1,3):
          try:
            user_answer = int(input(f"{num_1} + {num_2} = "))
            if user_answer == correct_answer:
               break
            else:
              print("EEE")
          except ValueError:
            print("EEE")
            continue
        
          
      else:
        score+=1
    except ValueError:
      print("EEE")
      for chance in range(1,3):
        try:
          user_answer = int(input(f"{num_1} + {num_2} = "))
          if user_answer == correct_answer:
            break
          else:
            print("EEE")
        except ValueError:
          print("EEE")
          continue
      print(f"{num_1} + {num_2} = {correct_answer}")
        
  print(f"Score: {score}")
        
    

 
        
          
      
      
def generate_integer(level):
  if level == 1 :
     num_1 = random.randint(1,9)
     num_2 =  random.randint(1,9)
     correct_answer = num_1 + num_2
     return [num_1,num_2,correct_answer]
  elif level == 2:
    num_1 = random.randint(10,99)
    num_2 =  random.randint(10,99)
    correct_answer = num_1 + num_2
    return [num_1,num_2,correct_answer]
  elif level == 3:
    num_1 = random.randint(100,999)
    num_2 =  random.randint(100,999)
    correct_answer = num_1 + num_2
    return [num_1,num_2,correct_answer]



if __name__ == "__main__":
    main()
      
       
   