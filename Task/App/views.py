# myapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm

def user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('home')  # Chuyển hướng đến trang chính sau khi đăng ký
        else:
            messages.error(request, 'Registration failed. Please correct the errors.')
    else:
        form = RegistrationForm()

    return render(request, '../App/templates/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')  # Chuyển hướng đến trang chính sau khi đăng nhập
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, '../App/templates/login.html')

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logout successful.')
    return redirect('login')  # Chuyển hướng đến trang đăng nhập sau khi đăng xuất
