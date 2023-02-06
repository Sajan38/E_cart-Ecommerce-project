import os
import uuid
from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')


# user Registeration
def registerview(request):
    if request.method=='POST':
        r=registerform(request.POST)
        if r.is_valid():
            us=r.cleaned_data["username"]
            em=r.cleaned_data["email"]
            pd=r.cleaned_data["password"]
            cd=r.cleaned_data["confirmpassword"]
            if pd==cd:
                l=registermodel(username=us,email=em,password=pd)
                l.save()
                return redirect(loginview)
            else:
                return HttpResponse("Register failed")
    return render(request,'register.html')



# user login
def loginview(request):
    if request.method=='POST':
        o=loginform(request.POST)
        if o.is_valid():
            us=o.cleaned_data["username"]
            pd=o.cleaned_data["password"]
            s=registermodel.objects.all()
            for i in s:
                if us==i.username and pd==i.password:
                    return redirect(userview)
            else:
                return HttpResponse("Login failed")
    return render(request,'login.html')


# user home page
def userview(request):
    a=uploadmodel.objects.all()
    im=[]
    pd=[]
    pr=[]
    di=[]
    id=[]
    for i in a:
        m=i.image
        im.append(str(m).split('/')[-1])
        p=i.productname
        pd.append(p)
        r=i.price
        pr.append(r)
        f=i.description
        di.append(f)
        o=i.id
        id.append(o)
    mylist=zip(im,pd,pr,di,id)
    return render(request,'userprofile.html',{'mylist':mylist})

def addcart(request,id):
    a=uploadmodel.objects.get(id=id)
    b=cartmodel(productname=a.productname,price=a.price,image=a.image,description=a.description)
    b.save()
    return redirect(cartdisplay)


# user cart display

def cartdisplay(request):
    id=[]
    pn=[]
    im=[]
    pr=[]
    di=[]
    a=cartmodel.objects.all()
    for i in a:
        x=i.id
        id.append(x)

        y=i.productname
        pn.append(y)

        z=i.image
        im.append(str(z).split ('/')[-1])

        p=i.price
        pr.append(p)

        d=i.description
        di.append(d)
    mylist=zip(im,pn,pr,di,id)
    return render(request,'cartdisplay.html',{'mylist':mylist})

# cart remove

def cartremove(request,id):
    a=cartmodel.objects.get(id=id)
    a.delete()
    return redirect(cartdisplay)

# cart buy

def cartbuy(request,id):
    a=cartmodel.objects.get(id=id)
    if request.method == 'POST':
        item_name=request.POST.get('productname')
        item_price=request.POST.get('price')
        item_quantity=request.POST.get('iquantity')
        total=int(item_price)*int(item_quantity)
        return render(request,'finalbill.html',{'in':item_name,'ip':item_price,'iq':item_quantity,'t':total})
    return render(request,'cartbuy.html',{'a':a})

def shopregview(request):
    if request.method=='POST':
        s=shopform(request.POST)
        if s.is_valid():
            sn=s.cleaned_data["shopname"]
            em=s.cleaned_data["email"]
            pd=s.cleaned_data["password"]
            cn=s.cleaned_data["confpassword"]
            if pd==cn:
                p=shopmodel(shopname=sn,email=em,password=pd)
                p.save()
                return redirect(shoploginview)
            else:
                return HttpResponse("Register failed")
    return render(request,'shopreg.html')


def shopregedit(request,id):
    a=shopmodel.objects.get(id=id)
    if request.method=='POST':
        a.shopname=request.POST.get('shopname')
        a.email=request.POST.get('email')
        a.password=request.POST.get('password')
        a.confpassword=request.POST.get('confpassword')
        a.save()
        return redirect(shoploginview)
    return render(request,'editshopreg.html',{'a':a})



def shoploginview(request):
    if request.method=='POST':
        u=shoploginform(request.POST)
        if u.is_valid():
            el=u.cleaned_data["email"]
            pd=u.cleaned_data["password"]
            y=shopmodel.objects.all()
            for i in y:
                id=i.id
                shop=i.shopname
                if el==i.email and pd==i.password:
                    return render(request,'shopprofile.html',{'id':id,'shop':shop})
            else:
                return HttpResponse("Login failed")
    return render(request,'shoplogin.html')




def shopprofile(request):
    return render(request,'shopprofile.html')




def shopupload(request):
    if request.method=='POST':
        a=uploadform(request.POST,request.FILES)
        if a.is_valid():
            pn=a.cleaned_data["productname"]
            pr=a.cleaned_data["price"]
            di=a.cleaned_data["description"]
            im=a.cleaned_data["image"]

            b=uploadmodel(productname=pn,price=pr,description=di,image=im)
            b.save()
            return redirect(viewproduct)
        else:
            return HttpResponse("item failed....")
    return render(request,'upload.html')

def viewproduct(request):
    a=uploadmodel.objects.all()
    li=[]
    pn=[]
    pr=[]
    di=[]
    id=[]
    for i in a:
        m=i.image
        li.append(str(m).split('/')[-1])
        p=i.productname
        pn.append(p)
        r=i.price
        pr.append(r)
        f=i.description
        di.append(f)
        o=i.id
        id.append(o)
    mylist=zip(li,pn,pr,di,id)
    return render(request,'viewproduct.html',{'mylist':mylist})


def productdelete(request,id):
    a=uploadmodel.objects.get(id=id)
    a.delete()
    return redirect(viewproduct)


def productedit(request,id):
    a=uploadmodel.objects.get(id=id)
    it=str(a.image).split('/')[-1]
    if request.method=='POST':
        if len(request.FILES)>0:
            if len(a.image)>0:
                os.remove(a.image.path)
            a.image=request.FILES['image']
        a.productname=request.POST.get('productname')
        a.price=request.POST.get('price')
        a.description=request.POST.get('description')
        a.save()
        return redirect(viewproduct)
    return render(request,'editproduct.html',{'a':a,'it':it})

                                          # Email
# ---------------------------------------------------------------------------------------------------------------

def regis(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')

        if User.objects.filter(username=username).first():

            messages.success(request,'username already taken')

            return redirect(regis)
        if User.objects.filter(email=email).first():
            messages.success(request,'email already exist')
            return redirect(regis)

        user_obj=User(username=username,email=email)
        user_obj.set_password(password)
        user_obj.save()
        auth_token=str(uuid.uuid4())
        profile_obj=profile.objects.create(user=user_obj,auth_token=auth_token)
        profile_obj.save()

        send_mail_regis(email,auth_token)
        return render(request,'success.html')
    return render(request,'register.html')



def send_mail_regis(email,auth_token):
    subject="your account has been verified"
    message=f'paste the link to verify your account http://127.0.0.1:8000/verify/{auth_token}'
    email_from=EMAIL_HOST_USER
    recipient=[email]
    send_mail(subject,message,email_from,recipient)



def verify(request,auth_token):
    profile_obj=profile.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        if profile_obj.is_verified:
            messages.success(request,'your account has been verified')
            return redirect(login)
        profile_obj.is_verified=True
        profile_obj.save()
        messages.success(request,'your account has been verified')
        return redirect(login)
    else:
        messages.success(request,'user not found')
        return redirect(login)


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username).first()

        if user_obj is None:
            messages.success(request,'user not found')
            return redirect(login)
        profile_obj = profile.objects.filter(user=user_obj).first()
        if not profile_obj.is_verified:
            messages.success(request, 'profile not verified check your mail')
            return redirect(login)
        user = authenticate(username=username, password=password)

        if user is None:
            messages.success(request,'wrong password or username')
            return redirect(login)
        return redirect(userview)
    return render(request,'login.html')

























