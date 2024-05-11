def main():
  userGreeting = input('Greeting:' ).lower().strip()
 
  if userGreeting[0:5] == 'hello' :
    print('$0')
  elif userGreeting[0] == 'h':
    print('20$')
  else:
    print('$100')


main()


