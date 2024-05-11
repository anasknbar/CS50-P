from tabulate import tabulate
import csv
import sys

def main():
  try:
    if len(sys.argv) == 2:
      if sys.argv[1][-3:] == 'csv':
        print(file_reader(sys.argv[1]))
      else:
        sys.exit("Not a Python file")
    elif len(sys.argv) > 2:
      sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
      sys.exit("Too few command-line arguments")
  except FileNotFoundError:
    sys.exit("File does not exist")
    
def file_reader(file_name):
  with open(file_name) as file:
    reader = csv.reader(file)
    headers = next(reader)
    table = list(reader)
    return(tabulate(table, headers, tablefmt="grid")) 
main()
  
  
# headers = ["Regular Pizza","Small","Large"]
#    table = [["Cheese","$13.50","$18.95"]]

# print(tabulate([['Cheese', '$25.50', '$39.95'], ['1 item', '$27.50', '$41.95'], ['2 items', '$29.50', '$43.95'], ['3 items', '$31.50', '$45.95'], ['Special', '$33.50', '$47.95']], headers, tablefmt="grid"))