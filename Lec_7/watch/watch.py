import re
import sys


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    matches = re.search(r'^(?:<iframe).*src="((https?://)?(www\.)?youtube.com/embed/.{11})".*>(?:</iframe>)$',s,re.IGNORECASE)
    if matches:
      final = re.sub(r"youtube.com/embed","youtu.be",matches.group(1))
      final = re.sub(r"https?","https",final)
      final = re.sub(r"(www\.)?","",final)
 
      return  final
    
     # return matches.group(1)
# http://youtube.com/embed/xvFZjo5PgG0
# https://youtube.com/embed/xvFZjo5PgG0
# https://www.youtube.com/embed/xvFZjo5PgG0


...


if __name__ == "__main__":
    main()
