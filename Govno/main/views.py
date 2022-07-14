from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def regist(request):
    return render(request, 'main/regist.html')


def test(request):
    return render(request, 'main/test.html')
