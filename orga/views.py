from django.shortcuts import render
from .models import Blog, review, products,contactus,Employee
# Create your views here.
from .healthybuddha import healthybuddha
from . communityfarm import communityfarm
from . greendna import greenda
from .organiceraa import organiceraa
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail,EmailMessage
import random
from orgaworks import settings
import pandas as pd
import pygsheets
import datetime
def home(request):
    getitemtablesmodel = products.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email  =request.POST.get('email')
        message = request.POST.get('message')   
        saving = contactus(name=name, email=email, message=message)
        saving.save()
    if request.method == 'GET':
        query= request.GET.get('q')
        if query is not None:
            lookups= Q(name__icontains=query) | Q(category__icontains=query) | Q(communityfarm__icontains=query) | Q(greendna__icontains=query) | Q(healthybuddha__icontains=query) | Q(organiceraa__icontains=query) | Q(freshfarm__icontains=query) 

            results= products.objects.filter(lookups).distinct()


            return render(request, 'search.html', {'results': results})

        else:
            return render(request, 'home.html',{'item':getitemtablesmodel})
    return render(request, 'home.html',{'item':getitemtablesmodel})
def vegetables(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email  =request.POST.get('email')
        message = request.POST.get('message')   
        saving = contactus(name=name, email=email, message=message)
        saving.save()
    getitemtablesmodel = products.objects.all()
    
    return render(request, 'pages/vegetables.html',{'item':getitemtablesmodel})
def exotic(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email  =request.POST.get('email')
        message = request.POST.get('message')   
        saving = contactus(name=name, email=email, message=message)
        saving.save()
    getitemtablesmodel = products.objects.all()
    return render(request, 'pages/exotic.html',{'item':getitemtablesmodel})
def fruits(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email  =request.POST.get('email')
        message = request.POST.get('message')   
        saving = contactus(name=name, email=email, message=message)
        saving.save()
    getitemtablesmodel = products.objects.all()
    return render(request, 'pages/fruits.html',{'item':getitemtablesmodel})
# start scarpings 
def productdescription(request,id):
    try:
        data=review.objects.filter(product=id).values()
        rev=data
    except:
        rev={}
    if(request.method=="POST") and "reviewsubmit" in request.POST:
        print("in post")
        name=request.POST.get("name")
        email=request.POST.get("email")
        userreview=request.POST.get("desc")
        productid=request.POST.get("productid")
        print(name,email,review,productid)
        review.objects.create(name=name,email=email,review=userreview,product=productid) 
    scrping_data  = products.objects.get(id=id)
    googlesheet=pygsheets.authorize(service_file="C://ORGAPLANTS//Scripts//orgaworks//orga//key2.json")
    sheet=googlesheet.open_by_url("https://docs.google.com/spreadsheets/d/1F2mYp4vb1MSxXYst2HnZS_W-ZmeZ9M9tsWBwmUVJtYE/edit#gid=0")
    sheetdate=datetime.date.today()
    print("crosed")
    sheetdate=sheetdate.strftime("%d/%m/%Y")
    try:
        if(sheet.worksheet_by_title(sheetdate)):
            print("inif")
            foundsheet=sheet.worksheet_by_title(sheetdate)
            if(foundsheet.find(scrping_data.name)):
                dataframe=foundsheet.get_as_df()
                requiredata=dataframe.loc[dataframe['PRODUCT'] == scrping_data.name]
                a=list(requiredata["COMMUNITYFARM"])
                print(a)
            
                return render(request, 'pages/productdescription.html',{'communityfarm_data1':list(requiredata["COMMUNITYFARM"])[0],'greenda_data1':list(requiredata["GREENDNA"])[0],'healthybuddha_data1':list(requiredata["HEALTHYBUDDHA"])[0],
                                                                    'organiceraa_data1':list(requiredata["ORGANICERAA"])[0],"proid":id,"review":rev,'linksdata':scrping_data,})


            else:
                print("inelse")
                sheetdata=pd.DataFrame()
                sheetdata["PRODUCT"]=[scrping_data.name,]
                communityfarm_data= communityfarm(scrping_data.communityfarm,"Onion")
                print(communityfarm_data)
                greenda_data= greenda(scrping_data.greendna,"Onion")
                print(greenda_data)
                healthybuddha_data= healthybuddha(scrping_data.healthybuddha,"Onion")
                print(healthybuddha_data)
                organiceraa_data= organiceraa(scrping_data.organiceraa,"Onion")
                print(organiceraa_data)
                sheetdata["Communityfarm"]=communityfarm_data.get("price")
                sheetdata["Greenda"]=greenda_data["price"]
                sheetdata["HealthyBuddha"]=healthybuddha_data["price"]
                sheetdata["Organiceraa"]=organiceraa_data["price"]
                
                sheetlist=sheetdata.values.tolist()
                print(sheetlist)
                foundsheet.append_table(values=sheetlist)
                return render(request, 'pages/productdescription.html',{'communityfarm_data':communityfarm_data,'greenda_data':greenda_data,'healthybuddha_data':healthybuddha_data,
                                                            'organiceraa_data':organiceraa_data,'linksdata':scrping_data,"proid":id,"review":rev})
            
    except:
        
        sheetdata=pd.DataFrame()
        sheetdata["PRODUCT"]=[scrping_data.name,]
        communityfarm_data= communityfarm(scrping_data.communityfarm,"Onion")
        greenda_data= greenda(scrping_data.greendna,"Onion")
        healthybuddha_data= healthybuddha(scrping_data.healthybuddha,"Onion")
        organiceraa_data= organiceraa(scrping_data.organiceraa,"Onion")
        sheetdata["Communityfarm"]=communityfarm_data.get("price")
        sheetdata["Greenda"]=greenda_data["price"]
        sheetdata["HealthyBuddha"]=healthybuddha_data["price"]
        sheetdata["Organiceraa"]=organiceraa_data["price"]
        
        
        sheet.add_worksheet(sheetdate)
        workingsheet=sheet.worksheet_by_title(sheetdate)
        defaultdata=["PRODUCT","COMMUNITYFARM","GREENDNA","HEALTHYBUDDHA","ORGANICERAA"]
        workingsheet.append_table(defaultdata,start='A1')
        sheetlist=sheetdata.values.tolist()
        
        workingsheet.append_table(values=sheetlist)
    
          
    return render(request, 'pages/productdescription.html',{'communityfarm_data':communityfarm_data,'greenda_data':greenda_data,'healthybuddha_data':healthybuddha_data,
                                                            'organiceraa_data':organiceraa_data,'linksdata':scrping_data,"proid":id,"review":rev})

def searchitems(request):
    getitemtablesmodel = products.objects.all()
    if request.method == 'GET':
        query= request.GET.get('q')
        if query is not None:
            lookups= Q(name__icontains=query) | Q(category__icontains=query) | Q(communityfarm__icontains=query) | Q(greendna__icontains=query) | Q(healthybuddha__icontains=query) | Q(organiceraa__icontains=query) | Q(freshfarm__icontains=query) 

            results= products.objects.filter(lookups).distinct()
         
            return render(request, 'pages/search.html', {'results': results,'search': query})

        else:
            return render(request, 'pages/search.html')

    else:
        return render(request, 'home.html',{'item':getitemtablesmodel})
def about(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email  =request.POST.get('email')
        message = request.POST.get('message')   
        saving = contactus(name=name, email=email, message=message)
        saving.save()
    return render(request, 'pages/about.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email  =request.POST.get('email')
        message = request.POST.get('message')   
        saving = contactus(name=name, email=email, message=message)
        saving.save()
    return render(request, 'pages/contactuspage.html')
    

def blog(request):
   getblogContent = Blog.objects.all()
   return render(request, 'pages/blog.html', {'getblogContent': getblogContent})


def internships(request):
    if(request.method=="POST") and "empsearch" in request.POST:
        empiddet=request.POST.get("empid")
        employeedata=Employee.objects.get(Employeeid=empiddet)
        employeename="Employee Name: "+employeedata.Fullname
        employeeemail="Email: "+employeedata.Email
        employeelinkedin="Linkedin: "
        employeerole="Role: "+employeedata.Role
        employeestatus="Employee Status: "+employeedata.Employee_Status
        linkedinlink=employeedata.Linkedin
        return render(request,"pages/intern.html",{"employeename":employeename,"employeeemail":employeeemail,
                                                   "employeelinkedin":employeelinkedin,"employeerole":employeerole,
                                                   "employeestatus":employeestatus,"linkedinlink":linkedinlink})
    if(request.method=="POST") and "apply" in request.POST:
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        job=request.POST.get("jobtitle")
        country=request.POST.get("country")
        state=request.POST.get("state")
        postal=request.POST.get("postal")
        experience=request.POST.get("experience")
        linkedin=request.POST.get("linkedin")
        empid="ORGA"+str(random.randint(1000,9999))
        resume=request.FILES.get("resume")
        print(resume.name,resume.content_type)
        message1="Name: {}\nRole: {}\nLinkedid: {} \nEmail: {}\nState: {}\nPhone:{}\n\nVisit Admin Panel to Update Employee Status".format(name,job,linkedin,email,state,phone)
        mail = EmailMessage("New Application", message1, settings.EMAIL_HOST_USER, ["thejasadithiya@gmail.com","sabarishkumar742@gmail.com"])
        mail.attach(resume.name,resume.read(),resume.content_type)
        mail.send()
        try:
            Employee.objects.create(Fullname=name,Email=email,phone=phone,Role=job
                                    ,Country=country,State=state,Zipcode=postal,
                                    Experience=experience,Linkedin=linkedin,Employeeid=empid,
                                    Resume=resume,Employee_Status="")
            message="Hi {} Thank You for Applying a role of {} at ORGAPLANTS your Application id is {}\n our Team will reach you within 2-3 days\n\n\nWith Regards\nTeam Recruitment\n ORGA PLANTS".format(name,job,empid)
                
            send_mail("OrgaPlants Careers",message,settings.EMAIL_HOST_USER,[email,])
            return render(request,"pages/intern.html",{"msg":"Thank You for applying we will get back to you as soon as possible!"})
        except:
            return render(request,"pages/intern.html",{"msg":"Something Went Wrong try again! or User Alredy Exist's"})
    return render(request,"pages/intern.html")
    
def Blogdescription(request,id):
    getblogContent   = Blog.objects.get(id=id)  
    if request.method == 'POST':
        name = request.POST.get('name')
        email  =request.POST.get('email')
        message = request.POST.get('message')   
        saving = contactus(name=name, email=email, message=message)
        saving.save()
    return render(request, 'pages/blogdescription.html',{'getcontent':getblogContent})

    
