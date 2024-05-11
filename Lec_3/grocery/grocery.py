grocery_list = []
def main():
  
  while True:
    try:
      user_items = input().lower().strip()
      adding(user_items)
      
    except EOFError:
      counting()
      
      break
  

def adding(item):
  grocery_list.append(item)
  
    
def counting():
  single_item_list = list(set((grocery_list)))
  ordered_list = sorted(single_item_list)
  for item in ordered_list:
    print(grocery_list.count(item), item.upper())
       
    
  
   
# def formating(list):
#   for item in list:
#     print(list.count(item))
#   print()
   

main()


  

    
    