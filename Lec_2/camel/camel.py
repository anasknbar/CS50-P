def main():
  user_input = input("camelCase: ")
  sneak_case = sneak_case_converter(user_input)
  print (sneak_case)
 
         



def sneak_case_converter(camelCase):
  snake_casing =''
  for char in camelCase:
    if(char.isupper()):
      snake_casing += f'_{char.lower()}'
    else:
      snake_casing += char
  return snake_casing

main()

