def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def main():
    while True:
        try:
            user_input = input("Fraction: ")
            numerator, denominator = user_input.split("/")
            if not (is_integer(numerator) and is_integer(denominator)):
                raise ValueError("Please enter a fraction with integer values.")
            cal = eval(user_input)
        except (ValueError, SyntaxError, NameError, ZeroDivisionError):
            continue
        else:
            break

    print(formating(cal))



def formating(result):
    percentage = result * 100
    rounded_percentage = round(percentage) 
    if rounded_percentage >= 99:
        return "F"
    elif rounded_percentage <= 1:
        return "E"
    else:
        return f"{rounded_percentage}%"

  
main()
# def main():
#   while True:
#     try:
#       user_inpuy = input("Fraction: ")
#       cal = eval(user_inpuy)
      
#     except ValueError:
#       continue
#     except SyntaxError :
#       continue
#     except NameError :
#       continue
#     except ZeroDivisionError:
#       continue
#     else:
#       break
    

#   print(cal)
   
  
  

 

# main()

# # input = '7.0'



# # print(float(input).is_integer())


