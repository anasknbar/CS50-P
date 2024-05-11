
def main():

  userInput = input("What time is it? ").strip()
  converted_time = convert(userInput)
  if 7 <= converted_time < 8:
    print("Breakfast time")
  elif 12 <= converted_time < 13:
    print("Lunch time")
  elif 18 <= converted_time < 19:
    print("Dinner time")


def convert(time):
   h,m = time.split(':')
   h = float(h)
   m = float(m)/60

   return h+m




    
if __name__ == "__main__":
    main()


#     convert succefully return decimal hours expected "7.5" not error/n >> this is my code def main():

#   userInput = input("What time is it? ").strip().split(':')
#   converted_time = convert(userInput)
#   if 7 <= converted_time < 8:
#     print("Breakfast time")
#   elif 12 <= converted_time < 13:
#     print("Lunch time")
#   elif 18 <= converted_time < 19:
#     print("Dinner time")

# def convert(time):
#     return (float(time[0])+float(time[1])/60)

# if __name__ == "__main__":
#     main()



