from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from members.forms import NewUserForm


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main_page')
        else:
            messages.success(request, "A logging error occured. Please check if you wrote your username or password correct")
            return redirect('login')
    else:
        return render(request, 'auth/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect('main_page')


def register_user(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, email=email, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered")
            return redirect('main_page')
    else:
        form = NewUserForm()
    return render(request, 'auth/register.html', {
        'form': form,
    })


