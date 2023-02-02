from django.shortcuts import render,HttpResponse,redirect
from myapp.models import TableEnquiry,JeCalc,Bill
from django.db.models import Sum
from datetime import date
import random
import  qrcode
from  pyzbar.pyzbar import decode
from PIL import Image
from django.contrib import messages
from playsound import playsound
import csv
# Create your views here.

def index(request):
    return render(request, 'index.html')

def newtest(request):
    bdata=JeCalc.objects.all() 
    gtotal=JeCalc.objects.all().aggregate(gtotaldata=Sum('total'))
    contex={
                'bdata':bdata,
                'gtotal':gtotal
            }          
    return render(request, 'newtest.html',contex)    


def bill(request):
    bdata=JeCalc.objects.all() 
    gtotal=JeCalc.objects.all().aggregate(gtotaldata=Sum('total'))
    g1total=JeCalc.objects.all().aggregate(gtotaldata=Sum('total')*0.03)  
    # grandtotal is dictionary, so we need to convert dictionary into float
    lst=[]
    for i in g1total:
        i2=(g1total[i])
        lst.append(i2)
        i3=round(i2,2)
    lst1=[]
    for i in gtotal:
        i4=(gtotal[i])
        lst1.append(i4)
        i4=round(i4,2)  
        
    grandtotal=i4+i3  

    today=date.today()
    
    cuid=random.sample(range(0,9),6)
    #cuid is list so we need to convert list to string
    listtostr=''.join(map(str,cuid))


    # we declare global variable for that vaiable use in another function
    global global_grandtotal,global_date,global_cus_id
    global_grandtotal=grandtotal
    global_date=today
    global_cus_id=listtostr

   
        


    contex={
                'bdata':bdata,
                'gtotal':gtotal,
                'i3':i3,
                'grandtotal':grandtotal,
                'today':today,
                'listtostr':listtostr,
                
                



            } 
    return render(request, 'bill.html',contex)  

def saveEnquiry(request):
    if request.method=="POST":
        name=request.POST.get("name")
        surname=request.POST.get("surname")    
        email=request.POST.get("email")    
        phone=request.POST.get("phone")    
        en=TableEnquiry(name=name,surname=surname,email=email,phone=phone)
        en.save()
    return render(request, 'index.html')

def jecalc(request):
    if request.method=="POST":
        
        sel=request.POST.get("sel")
        
        price=float(request.POST.get("price"))
        weight=float(request.POST.get("weight"))
        if price==0 or weight==0:
            return redirect('newtest')
      
        else:
           
            labour=weight*400
            labour=round(labour,2)
            total=(price*weight)+labour
            total=round(total,2)
            jc=JeCalc(price=price,weight=weight,total=total,sel=sel,labour=labour)
            jc.save()
            bdata=JeCalc.objects.all()
            
            gtotal=JeCalc.objects.all().aggregate(gtotaldata=Sum('total'))

            contex={
                'bdata':bdata,
                'gtotal':gtotal
            }
                    
    return render(request, 'newtest.html',contex)
        

def vdata(request):
    adata=JeCalc.objects.all().delete()               
    return render(request, 'newtest.html',{'adata':adata})

def dele(request,id):
    member=JeCalc.objects.get(id=id)
    member.delete()       
    return redirect('newtest')

    

def billdata(request):

    return redirect('bill')

# this prints() is for save button
def prints(request):
    if request.method=="POST":
    
        bname=request.POST.get("bname")
        bphone=(request.POST.get("bphone"))
        bemail=(request.POST.get("bemail"))

        strgrandtotal=str(global_grandtotal) 
        strdate=str(global_date)
        alldata='Phone='+bphone+' '+' Name='+bname+' '+'Email= '+bemail+' '+'Grandtotal= '+strgrandtotal+' '+'Purchase_Date= '+strdate+' '+'Customer_ID= '+global_cus_id
        
        generate_png=qrcode.make(alldata)
        generate_png.save('static/qrimages/'+global_cus_id+'.png')
     
        
        #  make qr code and save qrcode also
        save_prints=Bill(bname=bname,bphone=bphone,bemail=bemail,date=global_date,cus_id=global_cus_id,grandtotal=global_grandtotal)
        save_prints.save()

        

    return redirect('bill')


def qrdecoder(request):
    
    return render(request, 'qrdecoder.html')    

def decodefun(request):
    if request.method=="POST":
    
        cusidinput=request.POST.get("cusidinput")
        pngname='static/qrimages/'+cusidinput+'.png'
        
        decocdeQR=decode(Image.open(pngname))
        display_deocde=decocdeQR[0].data.decode('ascii')
        
     
        contex={
            'display_decode':display_deocde,
            
        }
    return render(request, 'qrdecoder.html',contex)        

 

def all_bills(request):
    all_billdata=Bill.objects.all()

    return render(request, 'all_bills.html',{'all_billdata':all_billdata}) 
         

def vieww(request,id):
    member=Bill.objects.get(id=id)
   
    name=member.bname
    phone=member.bphone
    email=member.bemail
    date=member.date
    cus_id=member.cus_id
    grandtotal=member.grandtotal
      
       
    contex={
        'name':name,
        'phone':phone,
        'email':email,
        'date':date,
        'cus_id':cus_id,
        'grandtotal':grandtotal,

    }
    return render(request,'view_bill.html',contex)

def searchbar(request):
    if request.method=="GET":
        query=request.GET.get("query")
        you_search=Bill.objects.filter(cus_id__contains=query)
    return render(request, 'search.html',{'you_search':you_search}) 
    
    # return (title__icontains=query)

def dvieww(request,id):
    member=Bill.objects.get(id=id)
    member.delete()       
    return redirect('all_bills')    

def vocabs(request):

    open_csv= open('voc1.csv','r')
    reader=csv.reader(open_csv)
    vocab_dict={}
    for row in reader:
        vocab_dict[row[0]]=row[1]
        print(vocab_dict)
    # my_dict ={
    #     'a':'aa',
    #     'b':'be',
    #     'c':'ce',
    #     'd':'de'

    # }
    random_dict=random.choice(list(vocab_dict.keys()))
    value_dict = vocab_dict.get(random_dict)
   
    global global_random_dict,global_value_dict
    global_random_dict=random_dict
    global_value_dict=value_dict

    contex={
        'random_dict':random_dict,
        'value_dict':value_dict,



    }
    return render(request, 'vocabs.html',contex)    

def vocab_check(request):
   

    englishinput=request.POST.get("englishinput")

    if englishinput==global_value_dict:
        playsound('yeahboy.mp3')     

        
    else:
        playsound('nono.mp3')     


    return redirect('vocabs')    


  

