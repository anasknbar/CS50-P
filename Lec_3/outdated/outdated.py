def main():
  while True:
    try:
     
      date = input("Date: ").strip()
      
      if "/" in date:
        slash_format(date)
        
      else:
        month_format(date)
        
        
    except (ValueError,TypeError):
      continue
    else:
      break
   
def slash_format(date_format):
  month,day,year = date_format.split("/")
  if int(month) > 12 or int(day) > 31:
    raise ValueError
  else:
    month = str(int(month)).zfill(2)
    day = str(int(day)).zfill(2)
    print(f"{year}-{month}-{day}")
 
  
    

   
def month_format(date):
  months = ["January","February","March","April","May",
    "June","July","August","September","October","November","December"]
  if "," not in date:
    raise ValueError
  month, day, year = date.replace(",","").split(" ")
 
  
  if month not in months or int(day) > 31:
    raise ValueError
  else:  
    month = months.index(month)+1
    month = str(int(month)).zfill(2)
    day = str(int(day)).zfill(2)
    print(f"{(year)}-{month}-{(day)}")
    

  
 

    
main()