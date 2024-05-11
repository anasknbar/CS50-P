import datetime
import sys




def main():
  try:
    user_input = (input("Date of Birth: "))
    print(converter(user_input))
    
  except ValueError:
    sys.exit("Invalid date")


def converter(date):
  # birth-day date
  b_year,b_month,b_day = date.split("-")
  b_year,b_month,b_day = int(b_year),int(b_month),int(b_day)
  # today-date
  today = str(datetime.date.today())
  t_year,t_month,t_day = today.split("-")
  t_year,t_month,t_day = int(t_year),int(t_month),int(t_day)
  
  x = int((datetime.date(t_year,t_month,t_day) - datetime.date(b_year,b_month,b_day)).total_seconds() / 60)
  
  
  
  return(x)  
  
  
  



if __name__ == "__main__":
    main()




