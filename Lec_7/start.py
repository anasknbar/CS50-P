import re

def main():
#   user_email = input("what's your email? ").strip()
#   # if re.search(r"^[a-zA-Z0-9_][a-zA-Z0-9_]*@[a-zA-Z0-9_][a-zA-Z0-9_]*\.(com|edu|gov|org|net)$",user_email,flags=0):
#   if re.search(r"^(\w+\.+)?\w+@(\w+\.+)?\w+\.(com|edu|gov|org|net)$",user_email,flags=0):
#   # if re.search(r"^colo(u|)r$",user_email,flags=0):
#     # 0- (..* = .+)
#     # 1- (".+@.+.com")
#     # .* >> zero or more repetition, that's mean if you write something befor and after the @ or you did not it's going to be acceptable. (@.com||abc@.com||@abc.com||abc@abc.com > all are acceptable)
#     # .+ >> to control that you need at least on repitions to accept the string (abc@abc.com is acceptable but @.com||abc@.com||@abc.com are not)
    
#     # 2- (r"^[a-zA-Z0-9_]*@[a-zA-Z0-9_]*\.(com|edu|gov|org|net)$") >> AAAA@BBBB.com, @.com >> vaild
#     # 3- (r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.(com|edu|gov|org|net)$") >> AAAA@BBBB.edu >> vaild, but @.com >> is not because you have to have at least one repitition or more 
#     # 4- (r"^[a-zA-Z0-9_]?@[a-zA-Z0-9_]?\.(com|edu|gov|org|net)$") >> a@b.com, @.com >> vaild, but aa@bb.com, or abc@dfg.com are not vaild
#     # 5- ([a-zA-Z0-9_] = \w. \w represent a word charchter,number and underscore)
#     # 6- \W, it's the oppisite, of \w, anything that is not  a word charchter,number or underscore 
    
#     print("Vaild")
#   else:
#     print("Not-Vaild")
  # while True:
  #   user_url = input("URL: ").strip()
  #   user_name = re.sub("^(https?://)?(www\.)?twitter\.(com|net|org)\W+","",user_url.lower())
  #   if not re.search(r"(https?://)?(www\.)?\w+\.(com|net|org)",user_name,flags=0):
 
  #     print(user_name)
  #     break
  #   else:
  #     continue
  
  # https://twitter.com/anasknbar
  # http://twitter.com/anasknbar
  # twitter.com/anasknbar
  # email = input("what's your email? ").strip()
  # # if re.search(r"^(\w|.)+@(\w|.)+\.edu$",email,re.IGNORECASE):
  # if re.search(r"^(\w|\.)+@(\w|\.)+\.edu$",email,re.IGNORECASE):
  #   print("vaild")
  # else:
  #   print("invalid")
  
  name =  input("what's your name? ").strip()
  
  if  matches := re.search(r"^(.+), ?(.+)$",name):
    print(matches.group(1).strip(),matches.group(2).strip())
main()
