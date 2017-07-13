# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response

# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader

import os


def charitiesList(request):
    return render_to_response('webapp/base.html')

def index(request):
    return HttpResponse("Hi!!!")