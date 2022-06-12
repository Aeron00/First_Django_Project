from django.shortcuts import redirect, render
from app1.forms import regForm,loginform
from app1.models import reg,login

# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    form=regForm
    return render(request, 'register.html', {'form':form, 'login_Page':'/login_page'})

def done(request):
    form=regForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('/show')

def show(request):
    information = reg.objects.all
    loginfo = login.objects.all
    return render(request,'show.html',{'information':information, 'login':loginfo})

def login_page(request):
    form=loginform
    return render(request, 'login.html',{'form':form, 'registration':'register'})

def loginsave(request):
    form=loginform(request.POST)
    if form.is_valid():
        form.save()
    return redirect('/show')  

def edit(request,id):
    data = reg.objects.get(id=id)
    return render(request,'edit.html',{'data':data})

def update(request,id):
    data=reg.objects.get(id=id)
    form=regForm(request.POST,instance=data)
    if form.is_valid():
        form.save()
    return redirect('/show')    

def delete(request,id):
    data=reg.objects.get(id=id)
    return render(request,'delete.html',{'data': data})

def deletedata(request,id):
    data=reg.objects.get(id=id)
    form=regForm(request.POST,instance=data)
    if form.is_valid():
        data.delete()
        form.save()
    return redirect('/show')
    
def search(request):
    Name = request.POST['uname']
    information = reg.objects.filter(uname__icontains=Name) or reg.objects.filter(id=Name)
    return render(request, 'show.html', {'information': information})
