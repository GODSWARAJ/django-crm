from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, Addrecordform
from .models import Record
# Create your views here.
def home(request):
    records = Record.objects.all()
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
    return render(request, 'home.html', {'records':records})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logout....")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered")
            return redirect('home')
    else:
        form = SignUpForm() 
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        #look up record
        customer_records = Record.objects.get(id = pk)
        return render(request, 'record.html', {'customer_records':customer_records})
    else:
        messages.success(request, "You must be login to view that page")
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        user = Record.objects.get(id = pk)
        user.delete()
        messages.success(request, "Record deleted successfully!")
        return redirect('home')
    else:
        messages.success(request, "YOU MUST BE LOGGED IN TO DO THAT..")
        return redirect('home')
    
def add_record(request):
    form = Addrecordform(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Record added successfully.....")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "YOU MUST BE LOGGED IN TO DO THAT..")
        return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id= pk)
        form = Addrecordform(request.POST or None, instance = record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully.....")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "YOU MUST BE LOGGED IN TO DO THAT..")
        return redirect('home')        