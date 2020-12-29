from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
def index(request):
    return render(request , 'index.html')

def about(request):
    return render(request , 'about us.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request , username=username , password=password)
        if user is not None:
            login(request,user)
            return redirect('..')
        else:
            messages.info(request , 'Username OR password is incorrect')
    return render(request , 'login(new).html')

   

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request , 'Account was created for '+ user)
            return redirect('login')
    context = {'form':form}   
    return render(request , 'register(new).html' , context)
