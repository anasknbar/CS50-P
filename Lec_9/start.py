# set

students = [
  {"name":"anas","house":"first"},
  {"name":"ahmad","house":"second"},
  {"name":"ali","house":"first"},
  {"name":"omr","house":"forth"},
  {"name":"rame","house":"second"},
  {"name":"moh","house":"fifth"},
  {"name":"salem","house":"forth"}
]

unique = []

for student in students:
  if student["house"] not in unique:
    unique.append(student["house"])
print(unique)