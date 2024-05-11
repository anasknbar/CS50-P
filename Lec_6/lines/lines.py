import sys
import csv

def main():
  try:
    if len(sys.argv) == 2:
      if sys.argv[1][-2:] == 'py':
        print(lines_of_code(sys.argv[1]))
      else:
        sys.exit("Not a Python file")
    elif len(sys.argv) > 2:
      sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
      sys.exit("Too few command-line arguments")
  except FileNotFoundError:
    sys.exit("File does not exist")
    
    
  
  


def lines_of_code(file_name):
  lines = []
  counter = 0
  with open(file_name) as file:
    for line in file:
      lines.append(line.strip())  
    for line in lines:
      if line != '' and line[0] != '#' and line[0] != '"""':
        counter += 1
    return(counter)
      
main()