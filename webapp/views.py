# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response

from webapp.models import Charity, Donation
from django.http import HttpResponse
from django.template import Context, loader
import calendar, datetime, json

## Pages ##

# Personal Profile Page
def my_profile(request):
    return render(request, "webapp/templates/index.html", {
        "monthly": monthly_donations(1),
        "top": top_charities(1),
        "sum": sum_donations(1),
        "user": 1
    })

# Zuora Profile Page 
def zuora_profile(request):
    return render(request, "webapp/templates/index.html", {
        "monthly": monthly_donations(0),
        "top": top_charities(0),
        "sum": sum_donations(0),
        "user": 0
    })

# Charity Page
def show_charities(request):
    if request.method == 'POST': 
        name = request.POST.get("charity_name")
        description = request.POST.get("charity_description")
        charity_object = Charity(name = name, description = description, votes = 0)
        charity_object.save()
    return render(request, 'webapp/templates/charities.html', {'charities':Charity.objects.all(), 'votes_left':2})

# New Charity Form Page
def new_charity(request):
	return render(request, 'webapp/templates/new_charity.html')

def charity_vote(request):
    votes_left = 0
    if request.method == 'POST': 
        id = request.POST.get("charity_id")
        charity_object = Charity.objects.get(pk=id)
        charity_object.votes += 1
        charity_object.save()
        votes_left = int(request.POST.get("votes_left"))
        votes_left -= 1
    return render(request, 'webapp/templates/charities.html', {'charities':Charity.objects.all(), 'votes_left':votes_left})

def top_charities(id):
    charities=Charity.objects.all();
    to_ret = []
    data = dict()
    for c in charities:
        sum=0
        charity_id=c.name
        for i in Donation.objects.all():
            print(i.charity)
        if id == 0:
            donations=Donation.objects.filter(charity__name=charity_id)
        else:
            donations=Donation.objects.filter(charity__name=charity_id).filter(user_id=1)
        for d in donations:
            sum=sum+d.amount
        if sum!=0:
            data[charity_id]=sum
    for k,v in data.items():
        to_ret.append({ 'label'.encode('utf8'): str(k).encode('utf8'), 'value'.encode('utf8'): str(v).encode('utf8') })
    return to_ret

def monthly_donations(id):
    to_ret=[]
    curr=datetime.datetime.now()
    curr_month=curr.month#current month
    curr_year=curr.year#current year
    for i in range(curr_month, 12):
        sum=0
        if id == 0:
            donations=Donation.objects.filter(date__month=i).filter(date__year=(curr_year-1))
        else:
            donations=Donation.objects.filter(date__month=i).filter(date__year=(curr_year-1)).filter(user_id=1)
        for d in donations:
            sum=sum+d.amount
        month=calendar.month_name[i][:3]
        to_ret.append({ 'month'.encode('utf8'): (month + ' ' + str(curr_year-1)).encode('utf8'), 'donation'.encode('utf8'): str(sum).encode('utf8') })
    for i in range(1, curr_month+1):
        sum=0
        if id == 0:
            donations=Donation.objects.filter(date__month=i).filter(date__year=(curr_year))
        else:
            donations=Donation.objects.filter(date__month=i).filter(date__year=(curr_year)).filter(user_id=1)
        for d in donations:
            sum=sum+d.amount
        month=calendar.month_name[i][:3]
        to_ret.append({ 'month'.encode('utf8'): (month + ' ' + str(curr_year)).encode('utf8'), 'donation'.encode('utf8'): str(sum).encode('utf8') })    
    return to_ret

def sum_donations(id):
    if id == 0:
        donations=Donation.objects.all()
    else:
        donations=Donation.objects.filter(user_id=1)
    sum=0
    for d in donations:
        sum=sum+d.amount
    return str(sum)

