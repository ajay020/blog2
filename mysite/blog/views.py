# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def blog_list(request):
    posts = Post.objects.all()
    context = {
    'posts':posts
    }
    return render(request,'blog/blog_list.html', context)
