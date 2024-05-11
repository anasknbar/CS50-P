import csv
import sys

def main():
  try:
    if len(sys.argv) == 3:
      if sys.argv[1][-3:] == 'csv' and sys.argv[2][-3:] == 'csv':
        file_reader(sys.argv[1],sys.argv[2])
      else:
        raise FileNotFoundError
    elif len(sys.argv) < 3:
      sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
      sys.exit("Too many command-line arguments")
  except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
    
def file_reader(file_name_1,file_name_2):
  names_list = []
  with open(file_name_1) as file:
    reader = csv.DictReader(file)
    for row in reader:
      last,first = row['name'].split(', ')
      house = row["house"]
      names_list.append({"first":first,"last":last,"house":house})
  
  with open(file_name_2,"w") as file:
    writer =  csv.DictWriter(file,fieldnames=["first","last","house"])
    writer.writeheader()
    for name in names_list:
      first = name["first"]
      last = name["last"]
      house = name["house"]
      writer.writerow({"house":house,"last":last,"first":first}) # changing the order will not affect the final result ass we specifiy the order from the fieldnames, 'you can type directly the object name'
      # writer.writerow(name)
      
if __name__ == "__main__":
    main()