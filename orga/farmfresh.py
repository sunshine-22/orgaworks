from bs4 import BeautifulSoup
import requests


def farmfresh(link,product):
    farmfresh={}
    try:
        farmfresh["product"]=product
        farmfresh["supplier"]="Farm Fresh"
        farmfresh["link"]=link
        r=requests.get(link)
        soup=BeautifulSoup(r.content,"html5lib")
        price=soup.option.text
        table=price.split("\n")
        price2=table[-2].replace(" ","")
        price3=price2.replace("-","")
        farmfresh["price"]=price3
        return farmfresh
    except:
        farmfresh["product"]=product
        farmfresh["supplier"]="Farm Fresh"
        farmfresh["link"]="Not Available"
        farmfresh["price"]="Not Available"
        return farmfresh
        
