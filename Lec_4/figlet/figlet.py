import sys
from pyfiglet import Figlet


def main():
  if len(sys.argv) == 1:
    user_text = input("Input: ")
    f = Figlet(font='acrobatic')
    print(f"Output: {f.renderText(user_text)}")
  elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
    try:
      
      font_type = sys.argv[2]
      f = Figlet(font=font_type)
      user_text = input("Input: ")
      print(f"Output: {f.renderText(user_text)}")
      
    except:
      sys.exit("Invalid usage")
      
  else:
     sys.exit("Invalid usage")
    

  
main()