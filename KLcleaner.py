import re
def clean():
    with open("log.txt",'r') as file:
        msg=file.read()

    msg=msg.replace(' ','')
    msg=re.sub(re.compile(r"<Key.space:''>  "),' ',msg)
    regex_key=re.compile(r'(<Key\..*?)(?:\'| \d|\"|Key.esc|\s)>(>?)')
    msg=re.sub(regex_key,'',msg)
    msg=msg.replace('\'','')
    msg=msg.replace(',','')
    print(msg)