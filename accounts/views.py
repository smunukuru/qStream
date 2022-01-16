from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        user_password = request.POST['user_password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']
        if user_password == confirm_password:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'user already taken...')
                return redirect('/accounts/register')
                # return HttpResponse('user already taken...<a href="/accounts/register">back</a>')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already exists...')
                return redirect('/accounts/register')
                # return HttpResponse('email already exists...<a href="/accounts/register">back</a>')
            else:
                user = User.objects.create_user(username=user_name, password=user_password, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save()
                return HttpResponse("<h1>user created successfully</h1>")

        else:
            messages.info(request, 'password not matched...')
            return redirect('/accounts/register')
            # return HttpResponse('password not matched...<a href="/accounts/register">back</a>')

    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/bakery/')
        else:
            messages.info(request, 'User and password doesnt match')
            return redirect('/accounts/login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/accounts/login')
