from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.
def create(request):
    a = studentFrom()
    b = students.objects.all()
    
    if request.method =='POST':
        a = studentFrom(request.POST)
        if a.is_valid():
            a.save()
        else:
            a = print('invaild input')
            
    else:
        a = studentFrom()
    return render(request,'index.html',{'abc':a,'data':b})

def update(request,id):
    c= students.objects.get(id=id)
    d = students.objects.all()
    e = studentFrom(instance=c)
    if request.method =='POST':
        a=studentFrom (request.POST,instance=c)
        if a.is_valid():
            a.save()
            return redirect ('/create')
        else:
            pass
    else:pass
    return render(request,'index.html',{'abc':e,'data':d})


def delete(request,id):
    c= students.objects.get(id=id)
    c.delete()
    return redirect('create')
    
