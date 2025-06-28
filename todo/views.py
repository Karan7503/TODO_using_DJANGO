from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required


def sign_in1(request):
    if request.method == "POST":
        u_name = request.POST.get('username')
        email = request.POST.get('email')
        pwd1 = request.POST.get('password')
        print( u_name, email, pwd1)
        user1 = User.objects.create_user(u_name,email,pwd1)
        user1.save()
        return redirect('/login1')

    return render(request, 'signup1.html')

def login1(request):
    if request.method == "POST":
        u_name = request.POST.get('username')
        pwd1 = request.POST.get('password')
        print(u_name,pwd1)
        user1 =authenticate(request, username=u_name,password = pwd1)
        if user1 is not None:
            login(request,user1)
            return redirect('/todo-page')
        else:
            return render(request, '/login1')

    return render(request, 'login1.html')

@login_required
def todopage1(request):
    if request.method == "POST":
        tname = request.POST.get('taskname')
        print(tname)
        title1 = models.TODO1(title = tname,user = request.user)
        title1.save()
        user = request.user
        res = models.TODO1.objects.filter(user = request.user).order_by('srno')
        return redirect('/todo-page',{'res':res})
    
    res = models.TODO1.objects.filter(user = request.user).order_by('srno')
    
        
    return render(request, 'todo1.html',{'res':res})

@login_required
def edit_task(request,srno):
    obj = models.TODO1.objects.get(srno = srno)
    if request.method == "POST":
        title1 = request.POST.get('updatetask')
        print(title1)
        obj.title = title1
        obj.save()
        
        return redirect('todo-page')
    return render(request, 'edit1.html',{'task':obj})

@login_required
def delete_task(request,srno):
    obj = models.TODO1.objects.get(srno = srno)
    obj.delete()
    return redirect('/todo-page')


def logout1(request):
    logout(request)
    return redirect('/login1')