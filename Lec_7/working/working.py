import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
  matches = re.search(r"^((([1-9])|10|11|12)(:(0?[0-9]|[1-5][0-9]))?) (AM|PM) to ((([1-9])|10|11|12)(:(0?[0-9]|[1-5][0-9]))?) (PM|AM)$",s)
  if  matches:

    match_1 = matches.group(1)
    match_2 = matches.group(6)
    match_3 = matches.group(7)
    match_4 = matches.group(12)
    return time_24(match_1,match_2) + " to " + time_24(match_3,match_4)
       
  else:
    raise ValueError

def time_24(t,m):
  if ':' in t:
    hour,minutes = t.split(":")
    if m == 'AM':
      if hour == '12':
        return '00:'+(minutes.zfill(2))
      else:
        return (hour.zfill(2))+':'+(minutes.zfill(2))
    else:
      if hour == '12':
        return '12:'+(minutes.zfill(2))
      else:
        return str(int(hour)+12)+':'+(minutes.zfill(2))
      
  else:
    if m == 'AM':
      if t == '12':
        return '00:00' 
      else:
        return t.zfill(2)+':00' 
    else:
      if t == '12':
        return '12:00'
      else:
        return str((int(t)+12))+':00'
    



if __name__ == "__main__":
    main()

 

    

