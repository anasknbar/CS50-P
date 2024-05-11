import uuid
import sys
import re
import random



# handle notFoundFileError


class Quiz():
  def __init__(self,name,n,time):
    self.name = name
    self.time = time
    self.n = n
    self.uuid = str(uuid.uuid4())[:7]
    self.write_exam_details()
    
  def write_exam_details(self):
    file_name = f'{self.uuid}_quiz_question.csv'
    with open(file_name,'a') as file:
        file.write(f"quiz_id,{self.uuid}\n")
        file.write(f"quiz_time,{self.time}\n")
        file.write(f"teacher name,{self.name}\n")
        file.write(f"-----------------------\n")
        file.write(f"question,correct answer, wrong answer, wrong answer, wrong answer, wrong answer\n")
    self.write_questions_to_file(file_name)
    
  def write_questions_to_file(self, filename):
    with open(filename, 'a') as file:
      for i in range(self.n):
        question = input(f'Question {i+1}: ').strip()
        answer = input(f'Correct answer {i+1}: ').strip().lower()
        wrong_answers = [input(f'Wrong answer {j+1}: ').strip().lower() for j in range(3)]
        file.write(f"{i+1}- {question},{answer},{','.join(wrong_answers)}\n")
    print(f'{self.name} quiz id is {self.uuid}')








  
  
  
  
    
class Student():
  def __init__(self,name,quiz_id):
    self.name = name
    self.quiz_id = quiz_id
    self.quiz_starter()
    
  # make it instance method
      
  def quiz_starter(self):
    
      file_name = f"{self.quiz_id}_quiz_question.csv"
      with open(file_name,'r') as file:
        start_line = 6
        student_answer_list = []
        for line_number, row in enumerate(file, start=1):
          # Skip lines until the starting line
          if line_number < start_line:
            continue
          else:
            student_answer_list.append(self.save_student_answer(row))
        self.answer_checker(student_answer_list)
        
          
  def save_student_answer(self,row):
    question,c_answer,r_answer_1,r_answer_2,r_answer_3 = row.split(',')
    multiple_chooses_list = [c_answer,r_answer_1,r_answer_2,r_answer_3.strip()]
    random.shuffle(multiple_chooses_list)
            
      
    student_answer = input(f"{question}\na-{multiple_chooses_list[0]}\nb-{multiple_chooses_list[1]}\nc-{multiple_chooses_list[2]}\nd-{multiple_chooses_list[3]}\nanswer >>> ").lower()
    return (
        {
        "question":question,
        "answer":c_answer.strip(),
        "student_answer":student_answer
        }
    )
            
            
  def answer_checker(self,answers):
     with open(f"{self.quiz_id}_student_answers.csv",'a') as file:
       file.write(f"student name,{self.name}\n")
       file.write(f"student score,{self.score(answers)}\n")
       file.write(f"question,correct answer,student answer\n")
       
       for answer in answers:
         file.write(f"{answer['question']},{answer['answer']},{answer['student_answer']}\n")
       file.write("______________\n")
         
  def score(self,answers):
    score = 0
    for answer in answers:
      if answer['answer'] == answer['student_answer']:
        score+=1
    return f"{score}/{len(answers)}"
  

 
  
def main():
 
 starter()
    




def starter():
  user_type = input('student(s) or teacher(t)? ').strip().lower()
  
  if user_type == 'teacher' or user_type == 't':
    teacher_name = input("Teacher Name: ")  
    quiz_question = input("Number of questions: ")
    quiz_time = input("Quiz time in minutes: ")
    try:
      quiz = Quiz(teacher_name,int(quiz_question),quiz_time)
    except ValueError:
      sys.exit("wrong input")
      
  elif user_type == 'student' or user_type == 's':
    student_name = input("Student Name: ")
    quiz_id = input("Enter the quiz id: ")
    student = Student(student_name,quiz_id)
      
  else:
    sys.exit('wrong input')

def add(a,b):
  return a+b

def multiply(a,b):
    return a * b


def divide(a,b):
    return a/b


if __name__ == "__main__":
    main()
