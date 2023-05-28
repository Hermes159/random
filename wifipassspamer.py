from pynput.keyboard import Key, Controller
keyboard = Controller()
list = ["pass2","pass1","pass3"]


wifi = input("Nome do wifi nabo!: ")
for i in list:
    print(f"netsh wlan set hostednetwork mode=allow SSID=({wifi}) key=({i})")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    print(f"netsh wlan connect name={wifi} SSID={wifi}")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    



        
        
        
        



 


    
