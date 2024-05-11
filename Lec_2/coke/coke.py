def main():
  
  coke = 50
  
  while True:
    user_input = int(input("Insert Coin: "))
    if user_input == 5 or user_input == 10 or user_input == 25 :
      coke -= user_input
      if coke > 0 :
        print(f"Amount Due: {coke}")
        continue
      else:
        print(f"Change Owed: {abs(coke)}")
        break
    else:
      print(f"Amount Due: {coke}")
      continue
    
main()



