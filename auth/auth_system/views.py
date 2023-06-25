from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib import messages

# Create your views here.
def homepage(request):
    return render(request, "auth_system/index.html", {})


def register(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname = request.POST.get('lname')
        name = request.POST.get('uname')
        email=request.POST.get('email')
        password=request.POST.get('pass')
        newuser = User.objects.create_user(username=name, email=email, password=password)
        newuser.first_name=fname
        newuser.last_name = lname

        newuser.save()
        return redirect("login")
    
    return render(request,"auth_system/register.html",{})

#def register(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        name = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        
        newuser = User.objects.create_user(username=name, email=email, password=password)
        newuser.first_name = fname
        newuser.last_name = lname
        
        newuser.save()
        return redirect("login")
    
    return render(request, "auth_system/register.html", {})


def login(request):
    if request.method=="POST":
        name = request.POST.get('uname')
        #email=request.POST.get('email')
        password=request.POST.get('pass')
        user = authenticate(username=name, password=password)
        if user is not None:
            # User credentials are valid, log in the user
            auth_login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('homepage')
        else:
            # User credentials are not valid, show an error message
            error_message = "Invalid username or password."
            messages.error(request, error_message)
            return render(request, "auth_system/login.html", {'error_message': error_message})
    return render(request,"auth_system/login.html",{})
