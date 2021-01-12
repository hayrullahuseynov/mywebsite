from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import BlogPost
from django.views.generic import ListView,DetailView
from django.urls import reverse_lazy
# Create your models here.


# Create your views here.
def read_article(request,id):
    obj = get_object_or_404(BlogPost, id=id)
    template_name = 'read_article.html'
    context = {'object': obj}
    return render(request, template_name, context)

def handler_404(request,exception):
    error = {"error":"404"}
    return render(request,"404.html",error)
    
def handler_400(request,exception):
    error = {"error":"400"}
    return render(request,"404.html",error)
    
def handler_403(request,exception):
    error = {"error":"403"}
    return render(request,"404.html",error)
    
def handler_500(request,exception):
   error = {"error":"500"}
   return render(request,"404.html",error)


