from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home/home.html", {})

def authorized(request):
    return render(request, "authorized.html", {})