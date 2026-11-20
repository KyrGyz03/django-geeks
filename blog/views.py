from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def helloWorld(request):
    if request.method == 'GET':
        return HttpResponse('Привет, это мой первый проект Django')

def about_me(request):
    if request.method == 'GET':
        return HttpResponse('Салам, я учусь Бэкэнду')