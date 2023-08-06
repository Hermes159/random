from stegano import lsb

def main():
    ste = input("""Please enter the name of the picture that you want to decode the text
(DISCLAIMER -> if you dont have the picture in the same folder type 1
            -> Only works with .png pics so dont need to add the extension to the name): """)
    if ste == "1":
        print("Well put the picture in the same folder or vice versa to avoid bugs")
        return 0
    message = lsb.reveal(f'{ste}.png')
    print(f"Message: {message}")

if __name__ == "__main__":
    main() 