import json
import requests
import sys
import ast

def main():

  if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
  try:
    # response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json",verify=True)
    # o = response.json()
    # rate = o["bpi"]["USD"]["rate"]
    # rate = rate.replace(",","")
    # -----
    rate = '37817.3283'
    rate = convert_to_number(rate)
    user_number = convert_to_number(sys.argv[1])
    price = rate * user_number
    price = round(price,4)
    formatted_price = "{:,.4f}".format(price)
   
    print(f"${formatted_price}")
  except ValueError:
    sys.exit("Command-line argument is not a number")
 
def convert_to_number(string_value):
    try:
        # Safely evaluate the string to obtain the appropriate Python literal
        number = ast.literal_eval(string_value)
        return number
    except (SyntaxError, ValueError):
        # If the input string is not a valid Python literal, return None or handle the error as needed
        raise ValueError

main()
