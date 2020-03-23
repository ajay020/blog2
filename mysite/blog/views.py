# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostCreateForm

def blog_list(request):
    posts = Post.objects.all()
    context = {
    'posts':posts
    }
    return render(request,'blog/blog_list.html', context)

def post_detail(request, id,slug):
    post = get_object_or_404(Post,id=id,slug=slug)
    context = {
    'post':post
    }
    return render(request,'blog/post_detail.html',context)
def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
    else :
        form  = PostCreateForm()

    context = {
    'form':form
    }
    
    return render(request,'blog/post_create.html',context)
