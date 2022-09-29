import requests
from bs4 import BeautifulSoup
class WebCrawler():
    def spider(self,input_from_user):
        r=1
        while r==1:
            page=1
            while page<=1:
                def get_single_item(item_url):
                    source_code=requests.get(item_url)
                    plain_code=source_code.text
                    soup=BeautifulSoup(plain_code)
                    for item_name in soup.findAll('div'):
                        print(item_name.string)
                url=input("Enter the URL including the http/https:\n")
                source_code=requests.get(url)
                plain_code=source_code.text
                soup=BeautifulSoup(plain_code)
                for link in soup.findAll('a'):
                    href=link.get('href')
                    get_single_item(url)
                    print(href)
            
        else:
            r=2
    
