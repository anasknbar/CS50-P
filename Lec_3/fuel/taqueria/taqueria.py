def main():
  price = 0
  while True:
    
    try:
     
      order = input("Item: ").title()
      y = kitchen(order)
      price += float(y)
    except EOFError:
      break
    except TypeError:
      continue
    else:
      form = "{:.2f}".format(price)
      print(f"Total: ${form}")
    

def kitchen(order):
  menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
  }
  
  for food in menu:
    if food == order:
      return menu[food]
    

    
  
main()