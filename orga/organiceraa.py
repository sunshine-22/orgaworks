from bs4 import BeautifulSoup
import requests


def organiceraa(link,product):
    organiceraa={}
    try:
        organiceraa["product"]=product
        organiceraa["supplier"]="Organiceraa"
        organiceraa["link"]=link
        r=requests.get(link)
        soup=BeautifulSoup(r.content,"html5lib")
        table=soup.findAll("span",{"id":"productPrice"})
        rc=str(table[0]).split(">")
        rc2=rc[2].replace("</span","")
        organiceraa["price"]=rc2
        return organiceraa
    except:
        organiceraa["product"]=product
        organiceraa["supplier"]="Organiceraa"
        organiceraa["link"]="Not Available"
        organiceraa["price"]="Not Available"
        return organiceraa
        
        
