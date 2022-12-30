from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'index.html', {})

def login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account done not exit plz sign in')

    return render(request,'users/login.html')

def register(request):

    if request.method == "POST":
        pass

    return render(request,'users/register.html')


def logout(request):
    #todo logic
    redirect('home')