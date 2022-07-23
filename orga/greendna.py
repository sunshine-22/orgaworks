from bs4 import BeautifulSoup
import requests

def greenda(link,product):
    greendadata={}
    try:
        greendadata["product"]=product
        greendadata["supplier"]="Greendna"
        greendadata["link"]=link
        r=requests.get(link)
        soup=BeautifulSoup(r.content,"html5lib")
        price=soup.option.text
        greendadata["price"]=price
        return greendadata
    except:
        greendadata["product"]=product
        greendadata["supplier"]="Greendna"
        greendadata["link"]="Not Available"
        greendadata["price"]="Not Avaiable"
        return greendadata
        
