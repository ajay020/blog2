# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404,reverse,redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth import login,authenticate,logout
from .forms import PostCreateForm,UserLoginForm
from django.http import HttpResponse,HttpResponseRedirect

def post_list(request):
    posts = Post.objects.all()
    context = {
    'posts':posts
    }
    return render(request,'blog/post_list.html', context)

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

def user_login(request):
    if request.method == 'POST':
        form  = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user  = authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('post_list'))
                else:
                    return HttpResponse("User is not active ")
            else:
                return HttpResponse("User is None")
    else:
            form = UserLoginForm()
            context = {
            'form':form
            }
            return render(request,'blog/login.html',context)

def user_logout(request):
    logout(request)
    return redirect('post_list')
