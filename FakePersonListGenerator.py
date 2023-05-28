from faker import Faker
fk = Faker()

def main():
    Persons()
    generator()
    
    
def Persons():
    global ni
    try:
        n = input("How many persons do you want generated in the text file?: ") 
        ni = int(n)
    except ValueError or NameError:
        n = input("Enter a valid input, please enter the number of how many persons you want generated: ")
        ni = int(n)


def generator():
    f = open("TotallyNormalList.txt","w")    
    ni1 = ni+1
    for i in range(1,ni1):
        f.write("\n" + fk.name() + "\n"+fk.address() + "\n")
        
    

if __name__ == "__main__":
    main()
