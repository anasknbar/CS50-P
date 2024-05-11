def main():
  while True:
    try:
      userGreeting = input('Greeting: ')
      bill = value(userGreeting)
      print(bill)
      break
    except IndexError:
      continue


def value(greeting):
  greeting = greeting.lower().strip()
  if len(greeting) != 0:
    if greeting[0:5] == 'hello' :
      return 0
    elif greeting[0] == 'h':
      return 20
    else:
      return 100
  else:
    raise IndexError
  
    


if __name__ == "__main__":
    main()
