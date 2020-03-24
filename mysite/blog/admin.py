# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from blog.models import Post,Profile

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','status')
    list_filter = ('status','created','updated')
    search_fields = ('author__username','title')
    prepopulated_fields = {'slug':('title',)}
    list_editable = ('status',)
    date_hierarchy = ('created')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'dob', 'photo')



admin.site.register(Post,PostAdmin)
admin.site.register(Profile,ProfileAdmin)
