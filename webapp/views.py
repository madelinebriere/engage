# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response

# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader
from .models import Donation, Charity
import calendar

import json

def dashboard(request):
    monthly = monthly_donations(request)
    top = top_charities(request)
    sum = sum_donations(request)
    return render_to_response("webapp/dashboard.html", {"monthly": monthly, "top": top, "sum": sum})


#Individual contributions!

def top_charities(request):
    #=Charity.objects.all();
    #if not charities:
        return default_top_charities(request) 
    #else:
        #TODO: Test
        #to_ret = []
        # data = dict()
        # for c in charities:
        #     sum=0
        #     charity_id=c.name
        #     donations=Donation.objects.filter(charity=charity_id)
        #     for d in donations:
        #         sum=sum+d.amount
        #     data[charity_id]=sum
        # top=sorted(dict, key=numbers.__getitem__, reverse=True)
        # top_char=top[1:5]
        # for k,v in data.items():
        #     to_ret.append({ 'label'.encode('utf8'): k.encode('utf8'), 'value'.encode('utf8'): str(v).encode('utf8') })
        #return to_ret

def monthly_donations(request):
    #TODO: Complete
    return default_monthly_donations(request)

def sum_donations(request):
    #TODO: Complete
    return default_sum_donations(request)

def default_monthly_donations(request):
    data = []
    for i in range(1,12):
        print(i)
        month=calendar.month_name[i][:3]
        data.append({ 'month'.encode('utf8'): month.encode('utf8'), 'donation'.encode('utf8'): str(1000+150*i).encode('utf8') })
    return data

def default_top_charities(request):
    data = []
    data.append({ 'label'.encode('utf8'): 'Ronald McDonald House'.encode('utf8'), 'value'.encode('utf8'): '15010.25'.encode('utf8') })
    data.append({ 'label'.encode('utf8'): 'Habitat For Humanity'.encode('utf8'), 'value'.encode('utf8'): '30045.02'.encode('utf8') })
    data.append({ 'label'.encode('utf8'): 'Save The Children'.encode('utf8'), 'value'.encode('utf8'): '20190.54'.encode('utf8') })
    return data    

def default_sum_donations(request):
    return "47245.81"

def charitiesList(request):
    return render_to_response('webapp/base.html')

def index(request):
    return HttpResponse("Hello, world. You're at charities.")
