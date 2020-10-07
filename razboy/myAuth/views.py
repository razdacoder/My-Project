from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import *


def index_view(request):
    return render(request, 'index.html')


def register_view(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        number = request.POST.get("number")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 == password2:
            if MyUser.objects.filter(email=email).exists():
                messages.info(request, "Email Already Exists")
                return redirect("register")

            elif MyUser.objects.filter(phone=number).exists():
                messages.info(request, "Email Already Exists")
                return redirect("register")
            else:
                user = MyUser.objects.create_user(
                    email=email,
                    fullname=fullname,
                    phone=number,
                    password=password1)
                user.save()
        else:
            messages.info(request, "Password do not match")
            return redirect("register")
        return redirect("home")


def login_view(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")

        else:
            messages.info(request, 'Invalid Email or Password')
            return redirect('login')


@login_required(login_url="login")
def logout_view(request):
    logout(request)
    return redirect('home')
