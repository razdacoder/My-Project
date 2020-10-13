from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import *
from main.models import *


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


@login_required(login_url="login")
def profile_view(request):

    qs = Ad.objects.filter(user=request.user)
    data = []

    for ad in qs:
        imgs = AdImage.objects.filter(ad=ad.id)
        ads = {"ad": ad, "images": imgs}
        data.append(ads)

    context = {
        "adData": data,
        # "art": artisan
    }

    if request.user.is_artisan == True:
        art = get_object_or_404(Artisan, user=request.user)
        artImages = GalleryImage.objects.filter(artisan=art.id)

        artisan = {
            "art": art,
            "images": artImages
        }
        context["art"] = artisan

    return render(request, 'profile.html', context)


@login_required(login_url="login")
def edit_pic_view(request):
    pic = request.FILES.get('pic')
    user = MyUser.objects.get(email=request.user.email)
    user.photo = pic
    user.save()
    return redirect("profile")


@login_required(login_url="login")
def edit_name_view(request):
    name = request.POST.get('fullname')
    user = MyUser.objects.get(email=request.user.email)
    user.fullname = name
    user.save()
    return redirect("profile")


@login_required(login_url="login")
def edit_mail_view(request):
    email = request.POST.get('email')
    user = MyUser.objects.get(email=request.user.email)
    user.email = email
    user.save()
    return redirect("profile")


@login_required(login_url="login")
def edit_phone_view(request):
    phone = request.POST.get('phone')
    user = MyUser.objects.get(email=request.user.email)
    user.phone = phone
    user.save()
    return redirect("profile")


@login_required(login_url="login")
def edit_pass_view(request):
    curr_pass = request.POST.get('currPass')
    new_pass = request.POST.get('newPass')
    new_pass_confirm = request.POST.get('newPassConfirm')
    user = MyUser.objects.get(email=request.user.email)
    if user.password == curr_pass:
        if new_pass == new_pass_confirm:
            user.set_password(new_pass)
            user.save()
            messages.success(request, "Password Changed Successfully!!")
            return redirect("profile")
        else:
            messages.error(request, "Passwords do not match")
            return redirect("profile")
    else:
        messages.error(request, "Incorrect Password")
        return redirect("profile")
