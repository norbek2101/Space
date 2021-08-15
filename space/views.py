from django.shortcuts import render
from .models import *
from .models import Blog


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def projects(request):
    project = Project.objects.all()
    context = {'projects': project}

    return render(request, 'projects.html', context)


def project_detail(request, pk):
    project = Project.objects.get(id=pk)

    return render(request, 'proj1.html', {'project': project})


def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}

    return render(request, 'blog.html', context)


def blog_detail(request, pk):
    blogs = Blog.objects.get(id=pk)

    return render(request, 'singlepost.html', {'blog': blogs})
