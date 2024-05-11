def main():
  userInput = input('File name: ').lower().strip().split(".")
  
  if(len(userInput) >= 2):
    if(userInput[-1] == 'gif'):
      print('image/gif')
    elif(userInput[-1] == 'png'):
      print('image/png')
    elif(userInput[-1] == 'jpg' or userInput[1] == 'jpeg'):
      print('image/jpeg')
    elif(userInput[-1] == 'pdf'):
      print('application/pdf')
    elif(userInput[-1] == 'zip'):
      print('application/zip')
    elif(userInput[-1] == 'txt'):
      print('text/plain')
    else:
      print('application/octet-stream')
  else:
    print('application/octet-stream')

main()