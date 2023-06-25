from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib import messages
import re 

# Create your views here.
def homepage(request):
    return render(request, "auth_system/index.html", {})


def register(request):
    ''' this the function for registraion of the user . here passworld must be a eight lenght long and must conation combination of number and character '''
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname = request.POST.get('lname')
        name = request.POST.get('uname')
        email=request.POST.get('email')
        password1=request.POST.get('pass1')
        password2=request.POST.get('pass2')
        if len(password1) >= 8 and re.search("[0-9]", password1) and re.search("[!@#$%^&*]", password1):
            if password1==password2:
                newuser = User.objects.create_user(username=name, email=email, password=password1)
                newuser.first_name=fname
                newuser.last_name = lname
                newuser.save()
                messages.success(request, "Registration successful. Please login.")
                return redirect("login")
            else:
                messages.error(request, "passworld don't match ") 
        else:
            messages.error(request, "Password must be at least 8 characters long and contain a special symbol  and a number.")
    return render(request,"auth_system/register.html",{})



def login(request):
    '''simple login from '''
    if request.method=="POST":
        name = request.POST.get('uname')
        password=request.POST.get('pass')
        user = authenticate(username=name, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('homepage')
        else:
            error_message = "Invalid username or password."
            messages.error(request, error_message)
            return render(request, "auth_system/login.html", {'error_message': error_message})
    return render(request,"auth_system/login.html",{})


def logout_view(request):
    '''log out from'''
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect("login")
