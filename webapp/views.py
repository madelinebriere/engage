# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def dashboard(request):
    return HttpResponse("DASHBOARD");

def charities_list(request):
    return HttpResponse("CHARITY");

def index(request):
    return HttpResponse("Hello, world. You're at charities.")
