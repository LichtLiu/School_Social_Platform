from django.shortcuts import render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from .models import Post
# Create your views here.

class PostList(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'index.html'
    context_object_name = 'blog_posts'

class PostDetail(DetailView):
    model = Post
    template_name = 'post/post_detail.html'


