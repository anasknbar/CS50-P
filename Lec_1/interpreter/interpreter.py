def main():
  userInput = input("Expression: ").split(" ")
  

  if(userInput[1] == '+'):
    print( float(userInput[0]) + float(userInput[2])) 
  elif(userInput[1] == '-'):
    print(float(userInput[0]) - float(userInput[2]))
  elif(userInput[1] == '*'):
    print(float(userInput[0]) * float(userInput[2]))
  elif(userInput[1] == '/'):
    print(float(userInput[0]) / float(userInput[2]))

main()