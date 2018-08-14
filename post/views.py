# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def create(request):
    return render(request, 'create.html', {})

def edit(request):
    return render(request, 'edit.html', {})

def delete(request):
    return render(request, 'delete.html', {})

def read(request):
    return render(request, 'read.html', {})

def list(request):
    return render(request, 'list.html', {})

def search(request):
    return render(request, 'search.html', {})