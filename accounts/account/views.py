from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
#view for home page
def home(request):
    return render(request,'account/home.html')
#view for landing page
def landing_page(request):
    return render(request,'account/landing_page.html')
#view for signup page
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'account/signup.html', {'form': form})
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #Add AuthenticationForm

def log_in(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request,'account/login.html', {"form":form})

def log_out(request):
    logout(request)
    return redirect('landing_page')





