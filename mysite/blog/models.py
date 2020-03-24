# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

class Post(models.Model):
    STATUS_CHOICES = (
      ('draft','Draft'),
      ('published','Published')
    )

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120)
    author = models.ForeignKey(User,related_name='blog_posts')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail",args=[self.id,self.slug])

@receiver(pre_save, sender=Post)
def pre_save_slug(sender, **kwargs):
    slug  = slugify(kwargs['instance'].title)
    kwargs['instance'].slug = slug

class Profile(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True,blank=True)
    photo = models.ImageField(null=True,blank=True)

    def __str__(self):
        return 'Profile of {}'.format( self.user.username )
