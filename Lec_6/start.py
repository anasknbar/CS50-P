import csv
# name = input("what's your name: ")

## file = open("names.txt","w")  
# open() will open the choosen file, and yet if it's not exiting it will create one open()  will return me what's called a 'file handle'.A file handle is a special value that allows you to interact with the opened file subsequently. It serves as a connection between your Python program and the file on the disk. Moreover, the 'w' means that this file is opend in a writing mode. ('w' it's dangerous, why?? )

## file = open("names.txt" ,"a") 
# "a" is for appending. How does it differ from "w"

## file.write(f"{name}\n") 
# write() is a method that comes with the open() function that allows me to write to the file

## file.close() 
# close the file, ensur that the file will not corrupted or deleted. use 'with' instead

# >> with syntax <<

# with open('names.txt',"a") as file :
#   file.write(f"{name}\n")
## in this method no need to close the file, it will close automatically
# names_list = []
# with open("names.csv","r") as file:
#   # for line in file:
#   #   print(line,end='') # or you can use readlines() methd on the file to return a list of lines
#   for line in file:
#     names_list.append(line.rstrip())

# for name in sorted(names_list):
#   print(name) 
  
# CSV is file type for storing data in releation and it stand for 'Comma Seperator Value'

# names = []
# with open("names.csv") as file:
#   for line in file:
#     name,age = line.rstrip().split(",")
#     names.append({"name":name,"age":age})
    
    # print(f"{name} is {age} years old")
   
 
# def get_name(student):
#    return student["name"]

# for name in sorted(names,key=get_name): # sort the dictionary based on its key, get_name main purpose is to feed the     sorted function with the names that will sort the dictioray based on.
#   print(f"{name['name']} is {name['age']}")

# you can get rid of the get_name function, if you are using it once and instead use lambda function(anonymous) as following.

# for name in sorted(names, key= lambda student_dic : student_dic["name"],reverse=True):
#   print(f"{name['name']} is {name['age']}")
  
  
# CSV library 
# students = []
# with open("names.csv") as file:
#   reader = csv.DictReader(file)
#   for row in reader:
#     students.append({'name':row['name'],'mark':row['mark']})
#     # print(f"{row['name'],row['mark']}")

# for student in sorted(students,key=lambda dic : int(dic["mark"])):
#   print(f"{student['name']} is {student['mark']} ")
  
# name = input("waht's your name? ")
# home = input("where's your home? ")

# with open("names.csv","a") as file:
#   writer = csv.writer(file)
#   writer.writerow([name,home])



with open("names.csv") as file:
  counter = 0
  reader = csv.reader(file)
  for line in reader:
    if len(line) != 0 and line[0][0] != '#':
      counter+=1
  print(counter)
  


























def dic_sorter(list_of_dic,sorted_by): # function takes argument to sort dic based on this argument
  def get(dic):
    return dic[sorted_by]
  for dic in sorted(list_of_dic,key=get):
    print(dic)
        
def update_file(person_name,new_age,file_name):
  updated = []
  with open(file_name) as file:
    for line in file:
      name,age = line.rstrip().split(",")
      if name == person_name:
        updated.append(f"{name},{new_age}")
      else:
        updated.append(f"{name},{age}")
  with open(file_name, "w"):
    pass  # Empty block does nothing, effectively truncating the file
       


  with open(file_name,"a") as file:
    
    for line in updated:
      file.write(f"{line}\n")
      

    
      
      

    


  
