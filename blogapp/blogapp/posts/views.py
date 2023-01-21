from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView
from django.views.generic.detail import DetailView 
from .models import Post
from django.views import generic
import datetime
from django.urls import reverse_lazy


class HomeView(ListView):
    model=Post
    template_name='posts/home.html'



class PostdetailView(DetailView):
    model=Post
    template_name='posts/detail.html'


class PostCreateView(CreateView):
    model = Post
    fields = ('__all__')
    template_name = 'posts/Post.html'

   
        


