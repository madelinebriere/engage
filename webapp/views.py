# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader

def dashboard(request):
    template = loader.get_template("webapp/dashboard.html")
    return HttpResponse(template.render(), {"section.title" : "Dashboard"});

def charitiesList(request):
    return HttpResponse("Hello, world. You're at charities.")

def index(request):
    return HttpResponse("Hello, world. You're at charities.")
