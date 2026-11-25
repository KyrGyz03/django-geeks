from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Blog


def helloWorld(request):
    if request.method == 'GET':
        return HttpResponse('Привет, это мой первый проект Django')

def about_me(request):
    if request.method == 'GET':
        return HttpResponse('Салам, я учусь Бэкэнду')

def blogMem_view(request):
    if request.method =='GET':
        blog = Blog.objects.all().order_by('-id')
    return render(request, 'blog_list.html', {'blog_list': blog})

def blogMem_detail(request, id):
    if request.method == 'GET':
        blog_id = get_object_or_404(Blog, id = id)
    return render(request, 'blog_detail.html', {'blog_id': blog_id})