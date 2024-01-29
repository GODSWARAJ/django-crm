from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticte
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "YOU HAVE BEEN LOGGED IN!")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in please try again")
            return redirect('home')
    return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logout....")
    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {})