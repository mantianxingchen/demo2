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
    post_id = request.GET.get('post_id')
    Post.objects.get(pk=post_id).delete()
    return redirect('/')

def read(request):
    post_id = request.GET.get('post_id')
    post = Post.objects.get(pk=post_id)
    return render(request, 'read.html', {'post':post})

def list(request):
    page = int(request.GET.get('page', 1))
    totle = Post.objects.count()
    per_page = 10
    pages = totle // 10 + 1
    start = (page - 1) * per_page
    end = start + per_page
    posts = Post.objects.all().order_by('-id')[start:end]  # 惰性加载
    return render(request, 'list.html', {'posts':posts, 'pages':range(pages)})

def search(request):
    keyword = request.POST.get('keyword')
    posts = Post.objects.filter(content__contains=keyword)
    return render(request, 'search.html', {'posts':posts})