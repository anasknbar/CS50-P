import string
def main():
    ...



def is_valid(plate):
    return length(plate) and first_two_char(plate) and no_punctuation_and_space(plate) and no_number_in_the_middle(plate)

def length(s):
    return 2 <= len(s) <= 6

def first_two_char(s):
    return s[:2].isalpha()

def no_punctuation_and_space(s):
    return not any(x in string.punctuation for x in s) and ' ' not in s

def no_number_in_the_middle(s):
    num_start_index = None
    for index, char in enumerate(s):
        if char.isdigit():
            num_start_index = index
            break

    if num_start_index is not None:
        num_str = s[num_start_index:]
        return num_str.isdigit() and num_str[0] != '0'
    return True
  



if __name__ == "__main__":
    main()

