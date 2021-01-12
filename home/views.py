from django.shortcuts import render
from blog.models import BlogPost
from django.views.generic import ListView,DetailView
from django.utils import timezone
from django.urls import reverse_lazy


def home(request):
    qs = BlogPost.objects.all().filter(published=True).order_by('-created_at')
    one = BlogPost.objects.last()
    template_name = 'home.html'
    latest = BlogPost.objects.filter(published=True).order_by('-created_at')[1:7]
    politics = BlogPost.objects.filter(categorie='Politics').order_by('-created_at')[:6]
    sport = BlogPost.objects.filter(categorie='Sport').order_by('-created_at')[:6]
    context = {'object_list': qs,
    "latest":latest,
    "one":one,
    'politics':politics,
    "sport":sport}
    return render(request, template_name, context)
def sport(request):
    bs = BlogPost.objects.filter(categorie='Sport').order_by('-created_at')
    template_name = 'categories.html'
    context = {'object_list':bs}
    return render(request,template_name,context)
def politics(request):
    bs = BlogPost.objects.filter(categorie='Politics').order_by('-created_at')
    template_name = 'categories.html'
    context = {'object_list':bs}
    return render(request,template_name,context)
def business(request):
    bs = BlogPost.objects.filter(categorie='Business').order_by('-created_at')
    template_name = 'categories.html'
    context = {'object_list':bs}
    return render(request,template_name,context)
def health(request):
    bs = BlogPost.objects.filter(categorie='Health').order_by('-created_at')
    template_name = 'categories.html'
    context = {'object_list':bs}
    return render(request,template_name,context)
def design(request):
    bs = BlogPost.objects.filter(categorie='Design').order_by('-created_at')
    template_name = 'categories.html'
    context = {'object_list':bs}
    return render(request,template_name,context)
def tech(request):
    bs = BlogPost.objects.filter(categorie='Tech').order_by('-created_at')
    template_name = 'categories.html'
    context = {'object_list':bs}
    return render(request,template_name,context)
def movies(request):
    bs = BlogPost.objects.filter(categorie='Movies').order_by('-created_at')
    template_name = 'categories.html'
    context = {'object_list':bs}
    return render(request,template_name,context)
