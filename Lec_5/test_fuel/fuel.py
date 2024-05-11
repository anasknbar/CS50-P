def main():
  while True:
    try:
      user_input = input('>>> ').strip()
      p = convert(user_input)
      print(gauge(p))
      break
    except (ValueError,ZeroDivisionError):
      continue
    

def convert(fraction):
    fraction_list = fraction.split('/')

    if fraction_list[0].isdigit() and fraction_list[1].isdigit() :
      if int(fraction_list[1]) == 0: 
        raise ZeroDivisionError
      elif int(fraction_list[0]) <= int(fraction_list[1]):
        percentage = int(round((int(fraction_list[0])/int(fraction_list[1])) ,2) * 100)
        return percentage
      else:
        raise ValueError
    else:
      raise ValueError
   

def gauge(percentage):
    if percentage <= 1:
      return "E"
    elif percentage >= 99:
      return "F"
    else:
      return f"{percentage}%"
    


if __name__ == "__main__":
    main()


# x = '100'
# print(int(x))
# print(x.isdigit())