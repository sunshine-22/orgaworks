from bs4 import BeautifulSoup
import requests
import re


def communityfarm(link,product):
    communityfarmdata={}
    try:
        communityfarmdata["product"]=product
        communityfarmdata["supplier"]="Community Farm"
        communityfarmdata["link"]=link
        page=requests.get(link)
        price=[]
        soup=BeautifulSoup(page.content,"html.parser")
        table=soup.findAll(text=re.compile("^₹"))
        for i in table:
            if(len(i)>1):
                price.append(i.replace("₹",""))
        communityfarmdata["price"]=max(price)
        return communityfarmdata
    except:
        communityfarmdata["product"]=product
        communityfarmdata["supplier"]="Community Farm"
        communityfarmdata["link"]="Not Available"
        communityfarmdata["price"]="Not Available"
        return communityfarmdata
        
        
    
    
