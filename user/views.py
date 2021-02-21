from django.shortcuts import render,redirect
from .forms import LoginForm,RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
# Create your views here.

def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form,
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username,password = password)
        if user is None:
            messages.info(request,"username or password is wrong !!!")
            return render(request,"login.html",context = context)
        login(request,user)
        messages.success(request,"Congratulations.You logged")
        return redirect("index")
    return render(request,"login.html",context = context)



def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username = username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        messages.success(request,"User saved")
        return redirect("index")
    return render(request,"register.html",{"form":form})


def logoutUser(request):
    logout(request)
    return redirect("index")