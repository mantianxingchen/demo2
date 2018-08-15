# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from post.models import Post

# Create your views here.
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(title=title, content=content)
        return redirect('/post/read/?post_id=%s' % post.id)
    else:
        return render(request, 'create.html', {})

def edit(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = Post.objects.get(pk=post_id)
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('/post/read/?post_id=%s' % post.id)
    else:
        post_id = request.GET.get('post_id')
        post = Post.objects.get(pk=post_id)
        return render(request, 'edit.html', {'post':post})

def delete(request):
    return render(request, 'delete.html', {})

def read(request):
    post_id = request.GET.get('post_id')
    post = Post.objects.get(pk=post_id)
    return render(request, 'read.html', {'post':post})

def list(request):
    return render(request, 'list.html', {})

def search(request):
    return render(request, 'search.html', {})