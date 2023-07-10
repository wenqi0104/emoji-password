from django.shortcuts import render

# Create your views here.
# login/views.py

from django.shortcuts import render, redirect

from portal import models
from . import globals


def index(request):
    return render(request, 'pages/index.html')


def login(request):
    # everytime login, clean the session cache
    globals.user_id = None
    request.session.flush()
    if request.method == "GET":
        return render(request, 'pages/login.html')
    else:
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        userinfo = models.User.objects.all()
        for i in userinfo:
            # authentication
            if i.username == username and i.password == pwd:
                globals.user_id = i.id
                request.session['username'] = i.username
                return redirect("/main")
        # return to the login page with the error message
        return render(request, 'pages/login.html', {'login_error': "unmatched username or password"})

def register(request):
    globals.user_id = None
    request.session.flush()
    if request.method == "GET":
        return render(request, 'pages/register.html')
    else:
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        # username and password verification
        if username == "" or pwd == "":
            return render(request, 'pages/register.html', {'register_error': "username or password is empty"})
        models.User.objects.create(username=username, password=pwd)
        # record the global username
        request.session['username'] = username
        return redirect("/main")


def logout(request):
    return redirect('/')
