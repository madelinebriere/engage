# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response

from webapp.models import Charity, Donation
from django.http import HttpResponse
from django.template import Context, loader
import calendar, datetime, json

## Pages ##

# Home Page
def index(request):
    return render(request, "webapp/templates/index.html", {
        "monthly": monthly_donations(request),
        "top": top_charities(request),
        "sum": sum_donations(request)
    })

# Charity Page
def show_charities(request):
	if request.method == 'POST': 
		name = request.POST.get("charity_name")
		description = request.POST.get("charity_description")
		charity_object = Charity(name = name, description = description, votes = 0)
		charity_object.save()
	return render(request, 'webapp/templates/charities.html', {'charities':Charity.objects.all()})

# New Charity Form Page
def new_charity(request):
	return render(request, 'webapp/templates/new_charity.html')

def charity_vote(request):
	if request.method == 'POST': 
		id = request.POST.get("charity_id")
		charity_object = Charity.objects.get(pk=id)
		charity_object.votes += 1
		charity_object.save()
	return render(request, 'webapp/templates/charities.html', {'charities':Charity.objects.all(), 'number':1})

def top_charities(request):
    charities=Charity.objects.all();
    if not charities:
        return default_top_charities(request) 
    else:
        #TODO: Test
        to_ret = []
        data = dict()
        for c in charities:
            sum=0
            charity_id=c.name
            donations=Donation.objects.filter(charity=c)
            for d in donations:
                sum=sum+d.amount
            data[charity_id]=sum
        #top=sorted(data, key=data.__getitem__, reverse=True)
        #top_char=top[1:5]
        for k,v in data.items():
            to_ret.append({ 'label'.encode('utf8'): k.encode('utf8'), 'value'.encode('utf8'): str(v).encode('utf8') })
        return to_ret

def monthly_donations(request):
    #TODO: Complete
    donations=Donation.objects.all();
    if not donations:
        return default_monthly_donations(request)
    else:
        to_ret=[]
        curr=datetime.datetime.now()
        curr_month=curr.month#current month
        curr_year=curr.year#current year
        months = dict()
        for i in range(curr_month, 12):
            sum=0
            donations=Donation.objects.filter(date__month=i).filter(date__year=(curr_year-1))#check syntax
            for d in donations:
                sum=sum+d.amount
            month=calendar.month_name[i][:3]
            months[month + ' ' + str(curr_year-1)]= sum#syntax
        for i in range(1, curr_month):
            sum=0
            donations=Donation.objects.filter(date__month=i).filter(date__year=curr_year)#check syntax
            for d in donations:
                sum=sum+d.amount
            month=calendar.month_name[i][:3]
            months[month + ' ' + str(curr_year)]= sum#syntax
        for k,v in months.items():
            to_ret.append({ 'label'.encode('utf8'): k.encode('utf8'), 'value'.encode('utf8'): str(v).encode('utf8') })
        return to_ret

def sum_donations(request):
    #TODO: Complete
    donations=Donation.objects.all();
    if not donations:
        return default_sum_donations(request);
    else:
        sum=0
        for d in donations:
            sum=sum+d.amount
        return str(sum)

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
