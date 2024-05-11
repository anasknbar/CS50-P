from validator_collection import validators, checkers, errors

def main():
  user_email = input("What's your email address? ")
  
  email_address = checkers.is_email(user_email)
  if email_address:
    print("Valid")
  else:
    print("Invalid")
  
if __name__ == "__main__":
    main()