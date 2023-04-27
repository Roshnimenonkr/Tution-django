from django.shortcuts import render,get_object_or_404,redirect
from .models import Client,Tutor,Library,RequestDemo,BookClass,DemoCo
from django.contrib import messages
import decimal


def home(request):
    return render(request,'home.html')

def log(request):
    if request.method=="POST":
        try:
            client_details=Client.objects.get(Email=request.POST['email'],Password=request.POST['password'])
            request.session['email']=client_details.Email
            request.session['user']=client_details.Name
            request.session['standard']=client_details.Standard

            return render(request,'studenthome.html')
        except Client.DoesNotExist as e:
            messages.info(request,"Invalid User")
            return render(request,"signin.html")  
    return render(request,'signin.html')


def reg(request):
    if request.method=='POST':
        name=request.POST['Name']
        email=request.POST['email']
        standard=request.POST['standard']
        phone=request.POST['phone']
        password=request.POST['pass']
        cpass=request.POST['re_pass']
        emailexist=Client.objects.filter(Email=email)
        phoneexist=Client.objects.filter(Phone=phone)
        passwordexist=Client.objects.filter(Password=password)
        if emailexist:
            messages.info(request,"Email already exist")
            return render(request,"signup.html")
        elif phoneexist:
            messages.info(request,"Phone Number already exist")
            return render(request,"signup.html")
        elif password!=cpass:
            messages.info(request,"Password entered are different")
            return render(request,"signup.html")
        else:
            Client(Name=name,Email=email,Standard=standard,Phone=phone,Password=password,ConPassword=cpass).save()
    return render(request,'signup.html')


def logtutor(request):
    if request.method=="POST":
        try:
            tutor_details=Tutor.objects.get(Username=request.POST['username'],Password=request.POST['password'])
            request.session['username']=tutor_details.Username
            request.session['tutoro']=tutor_details.Name
            request.session['price']=tutor_details.Price
            return render(request,'tutorhome.html')
        except Client.DoesNotExist as e:
            messages.info(request,"Invalid User")
            return render(request,"tutorsignin.html")  
    return render(request,'tutorsignin.html')



def studentHome(request):
    return render(request,'studenthome.html')


def ViewTutor(request):
    tutor = Tutor.objects.all().values()
    context={
        'tutor':tutor
    }
    return render(request,'viewtutor.html',context)


def Tutordetail(request,tutor_id):
    detail=get_object_or_404(Tutor,id=tutor_id)
    request.session['tutoro']=detail.Name
    request.session['sub']=detail.Subject
    request.session['tutor_id']=detail.id
    request.session['price']=detail.Price
    return render(request,'tutordetail.html',{'detail':detail})


def Requestdemo(request):
    student=request.session['user']
    tutor=request.session['tutoro']
    standard=request.session['standard']
    subject=request.session['sub']
    
    context={
        'student':student,
        'standard':standard,
        'tutor':tutor,
        'subject':subject
    }
    if request.method=='POST':
        student=request.POST['student']
        standard=request.POST['standard']
        tutor=request.POST['tutor']
        subject=request.POST['subject']
        date=request.POST['date']
        time=request.POST['time']
       
        exist=RequestDemo.objects.filter(student=student,tutor=tutor)
        if exist:
            messages.info(request,"already exist")
            return render(request,"requestdemo.html")
        else:
            RequestDemo(student=student,standard=standard,tutor=tutor,subject=subject,date=date,time=time).save()
    return render(request,'requestdemo.html',context)


def BookTutor(request):
    student=request.session['user']
    tutor=request.session['tutoro']
    standard=request.session['standard']
    subject=request.session['sub']
    price=request.session['price']
    
    if request.method=='POST':
        student=request.POST['student']
        standard=request.POST['standard']
        tutor=request.POST['tutor']
        subject=request.POST['subject']
        date=request.POST['date']
        time=request.POST['time']
        total_time=request.POST['total_time']
        price=request.POST['price']
        exist=BookClass.objects.filter(student=student,tutor=tutor)
        if exist:
            messages.info(request,"already exist")
            return render(request,"booktutor.html")
        else:
            BookClass(student=student,standard=standard,tutor=tutor,subject=subject,date=date,time=time,total_time=total_time,price=price).save()
            return redirect('PaidTutor')
    context={
        'student':student,
        'standard':standard,
        'tutor':tutor,
        'subject':subject,
        'price':price
        }
    return render(request,'booktutor.html',context)

def PaidTutor(request):
    student=request.session['user']
    tutor=request.session['tutoro']
    price=request.session['price']
    detail=get_object_or_404(BookClass,student=student,tutor=tutor)
    request.session['time']=detail.total_time
    ttime=request.session['time']
    amount=price*ttime
    context={
        'detail':detail,
        'amount':amount
        }
    return render(request,'paidtutor.html',context)

def Classtime(request):
    student=request.session['user']
    req=RequestDemo.objects.filter(student=student)
    bok=BookClass.objects.filter(student=student)
    context={
        'req':req ,
            'bok':bok    }
    return render(request,'classtime.html',context)

def StudentBooks(request):
    student=request.session['user']
    print(request.session['user'])
    bok=BookClass.objects.filter(student=student)
    if bok:
        new=Library.objects.all().values()
        return render(request,'studentbooks.html',{'new':new})
    else:
        messages.info(request,"You can not Access this facility now")
        return render(request,"studenthome.html")
    # for b in bok:
    #     request.session['sub']=b.subject
    #     Subject=request.session['sub']
    #     new=Library.objects.filter(Subject=Subject)
    #     context={
            
    #         'new':new
    #         }
    #     print(context)
    #     return render(request,'demo.html',context)



def TutorHome(request):
    tutor_id=request.session['tutor_id']
    tutor=Tutor.objects.filter(id=tutor_id)
    
    context={
        'tutor':tutor}
    return render(request,'tutorhome.html',context)


def Tutorrequest(request):
    name=request.session['tutoro']
    req=RequestDemo.objects.filter(tutor=name)
    bok=BookClass.objects.filter(tutor=name)
    context={
        'req':req,
        'bok':bok     }
    return render(request,'tutorrequest.html',context)


def remove(request,Req_id):
    if request.method=='GET':
        cp=get_object_or_404(RequestDemo,id=Req_id)
        student=cp.student
        tutor=cp.tutor
        subject=cp.subject
        standard=cp.standard
        date=cp.date
        time=cp.time
        DemoCo(student=student,tutor=tutor,subject=subject,standard=standard,date=date,time=time).save()
        cp.delete()
    return redirect('Tutorrequest')

def Democomplete(request):
    tutor=request.session['tutoro']
    detail=DemoCo.objects.filter(tutor=tutor)
    return render(request,'democomplete.html',{'detail':detail})

def TutorLibrary(request):
    books=Library.objects.all().values()
    return render(request,'tutorlibrary.html',{'books':books})



def logout(request):
    del request.session["user"]
    return redirect('home')
    


def logouttutor(request):
     del request.session["username"]
     return redirect('home')