from bs4 import BeautifulSoup
import requests


def healthybuddha(link,product):
    healthydata={}
    try:
        healthydata["product"]=product
        healthydata["supplier"]="Healthy Buddha"
        healthydata["link"]=link
        r=requests.get(link)
        soup=BeautifulSoup(r.content,"html5lib")
        data=soup.option.text
        healthy_GetPrice = data[30:]
        healthy_GetPrice =healthy_GetPrice.replace(" ","")
        healthy_GetPrice =healthy_GetPrice.replace("-","")
        healthy_quantity = data[0:20]
        healthydata["price"]=healthy_GetPrice
        return healthydata
    except:
        healthydata["product"]=product
        healthydata["supplier"]="Healthy Buddha"
        healthydata["link"]="Not Available"
        healthydata["price"]="Not Available"
        return healthydata
        
        
