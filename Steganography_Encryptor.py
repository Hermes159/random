from stegano import lsb

def main():
    ste = input("""Please enter the name of the picture that you want to hide the text
(DISCLAIMER -> if you dont have the picture in the same folder type 1
            -> Only works with .png pics so dont need to add the extension to the name): """)
    if ste == "1":
        print("Well put the picture in the same folder or vice versa to avoid bugs")
        return 0
    steo = input(f"Do you want to change the name of the output image?(if you want to use the default'{ste}_B' type 1, otherwise type the name that you want)")
    if steo == "1":
        OutputImage = f"{ste}_B.png"
        message_to_hide = input("Please enter the message that you want to hide: ")
        image_to_hide = f"{ste}.png"
        lsb.hide(image_to_hide, message=message_to_hide).save(OutputImage)
        return 0
    OutputImage = f"{steo}.png"
    message_to_hide = input("Please enter the message that you want to hide: ")
    image_to_hide = f"{ste}.png"
    lsb.hide(image_to_hide, message=message_to_hide).save(OutputImage)



if __name__ == "__main__":
    main() 
    
    
        
    
    
    



