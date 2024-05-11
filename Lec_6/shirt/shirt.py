from PIL import Image,ImageOps
import sys
import re

def main():
    try:
        validation(sys.argv)
    except FileNotFoundError:
        sys.exit("Input does not exist")
              
def validation(arg_list):
    if len(arg_list) < 3:
        sys.exit("Too few command-line arguments")
    elif len(arg_list) > 3:
        sys.exit("Too many command-line arguments")
    else:
        matches_1 = re.search(r".+\.{1}(jpg|jpeg|png)",arg_list[1],re.IGNORECASE) 
        matches_2 = re.search(r".+\.{1}(jpg|jpeg|png)",arg_list[2],re.IGNORECASE)
        

        if matches_1 and matches_2 :
            if(matches_1.group(1) == matches_2.group(1)):
                cs50_shirt(arg_list)
                # print(sys.argv)
            else:
                sys.exit("Input and output have different extensions")
        else:
            sys.exit("Invalid output")  

def cs50_shirt(path):
    
    overlay_image = Image.open("shirt.png")
    base_image = Image.open(path[1])
    target_size = (600,600)
    # make the base image dimentions same as ovelay image
    resized_base_image = ImageOps.fit(base_image, target_size,method=0,bleed=0.0,centering=(0.5,0.5))
    
    position = ((resized_base_image.width - overlay_image.width) // 2, (resized_base_image.height - overlay_image.height) // 2)
    
    resized_base_image.paste(overlay_image,position,overlay_image)
    
    resized_base_image.save(f"muppet_0{naming_output(path[1])}.jpg")
    
def naming_output(before_num):
    
    matches = re.search(r"muppet_0([0-9])\.(?:png|jpg|jpeg)",before_num)
    return(matches.group(1))
    
    
    
    
    
    
   
    
main()








