# user_input = input("what's your name? ")

# with open('names.txt','a') as file:
#   file.write(f"{user_input}\n")

# --------------------------------------------



# --------------------------------------------

# names = []
# with open('names.txt','r') as file:
# lines = file.readlines() >> give you a list of lines from the names.txt
#   for line in file:
#     names.append(line)
# for name in names:
#   print(name.strip())

# --------------------------------------------

# with open('names.txt','r') as file:
#   for line in sorted(file,reverse=True):
#     print(line,end='')

# -------------------CSV files----------------------
with open('students.csv') as file:
  for line in sorted(file):
    name,school = line.rstrip().split(',')
    print(f"{name} study in {school}")















# function 

# edited_version = list() 
# with open('students.csv') as file:
#   for line in file:
#     name,school = line.strip().split(',')
#     if name == 'ahmad' and school == 'Moonlight':
#       edited_version.append(f'rame,{school}')
#     else:
#       edited_version.append(f"{name},{school}")

# with open("students.csv",'w') as file:
#   pass
# with open("students.csv",'a') as file:
#   for line in edited_version:
#     file.write(f"{line}\n")
      
  

  

