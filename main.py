from colorama import Fore, Back, Style
import keylogger
import portscanner
import webcrawler
import cipher
import operatingsys

r=1

while r==1:
    import platform
    my_os=platform.system()
    with open('myOS.txt','w') as file:
        file.writelines(str(my_os))
    with open('myOS.txt','r') as file:
        lines=file.read()
        first=lines.split('\n',1)[0]
        print(first)
        if(first=='Windows'):
            import os
            os.system('cls')
        else:
            import os
            os.system('clear')
    print(Fore.GREEN+"""
 .o88b. d8888b. db    db d8888b. d888888b  .d8b.  d8888b. db    db  .d8b.  d8b   db  .o88b. d88888b 
d8P  Y8 88  `8D `8b  d8' 88  `8D `~~88~~' d8' `8b 88  `8D 88    88 d8' `8b 888o  88 d8P  Y8 88'     
8P      88oobY'  `8bd8'  88oodD'    88    88ooo88 88   88 Y8    8P 88ooo88 88V8o 88 8P      88ooooo 
8b      88`8b      88    88~~~      88    88~~~88 88   88 `8b  d8' 88~~~88 88 V8o88 8b      88~~~~~ 
Y8b  d8 88 `88.    88    88         88    88   88 88  .8D  `8bd8'  88   88 88  V888 Y8b  d8 88.     
 `Y88P' 88   YD    YP    88         YP    YP   YP Y8888D'    YP    YP   YP VP   V8P  `Y88P' Y88888P 
            """)
    print("HI !!! This is an advanced tool. Please select what you want to do:")
    print("1. Use Web Crawler")

    print("2. Start the Advanced Keylogger")
    
    print("3. Know your Operating System")

    print("4. Break Ciphers")
    print("5. Port Scanner")

    print("10. Exit")

    input_from_user = int(input("[+]Enter a number from 1 to 5:"))
    if input_from_user==1:

        obj = webcrawler.WebCrawler()

        obj.spider(input_from_user)

    if input_from_user==2:

        obj = keylogger.KeyLogger()

        obj.KeyLog(input_from_user)
    if input_from_user==3:
        obj = operatingsys.OperatingSys()
        obj.OPeratingSys(input_from_user)
    if input_from_user == 4:

        obj = cipher.Cipher()

        obj.Cypher(input_from_user)
    if input_from_user==5:
        obj=portscanner.PortScanner()
        obj.POrtScanner(input_from_user)
    else:

        r = 2

