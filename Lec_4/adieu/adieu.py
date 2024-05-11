import inflect
p = inflect.engine()
def main():
  names_list = []
  while True:
    try:
      name = input("Name: ").strip()
      names_list.append(name)
    except EOFError:
      adieu(names_list)
      break




      

def adieu(list):
  # >>> withut using libary
  # if len(list) == 1: 
  #   print(f"\nAdieu, adieu, to {list[0]}")
  # elif len(list) == 2:
  #   print(f"\nAdieu, adieu, to {list[0]} and {list[1]}")
  # elif len(list) > 2:
  #   names_str = ""  
  #   for i in range(1, len(list)-2):
  #     names_str += list[i]+", "
  #   print(f"\nAdieu, adieu, to {list[0]}, {names_str}{list[-2]} and {list[-1]}")
  mylist = p.join((list), final_sep=",")
  print("Adieu, adieu, to",mylist)

  
main()