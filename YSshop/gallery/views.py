from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def add(request):
    return render(request, 'add.html')


def detail(request):
    return render(request, 'detail.html')


def done(request):
    return render(request, 'done.html')


def error(request):
    return render(request, 'error.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')
