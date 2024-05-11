import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))

def validate(ip):
    if re.search(r"^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})$",ip,flags=0):
      return True
    else:
      return False


if __name__ == "__main__":
    main()

