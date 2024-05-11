def main():
  x = int(input("what's x? "))
  print("x square is",square(x))
  
def square(n):
  return n * n

if __name__ == "__main__":
  main()
  
  
  # def write_questions_to_file(self,file_name):
  #   for i in range(self.n):
  #     self.question = input(f'question {i+1}: \n').strip()
  #     self.answer = input(f'correct answer {i+1}: \n').strip()
  #     self.wrong_answer_1 = input(f'wrong answer 1 : \n').strip()
  #     self.wrong_answer_2 = input(f'wrong answer 2 : \n').strip()
  #     self.wrong_answer_3 = input(f'wrong answer 3 : \n').strip()
  #     with open(file_name,'a') as file:
        
  #       file.write(f"{i+1}- {self.question},{self.answer},{self.wrong_answer_1},{self.wrong_answer_2},{self.wrong_answer_3}\n")
        
  #   print(f'{self.name} quiz id is {self.uuid}')