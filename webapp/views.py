# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response

from webapp.models import Charity
from pprint import pprint
# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader
from django.template import RequestContext

def dashboard(request):
    return render_to_response("webapp/dashboard.html")

def charitiesList(request):
	if request.method == 'POST': 
		name = request.POST.get("charity_name")
		description = request.POST.get("charity_description")
		charity_object = Charity(name = name, description = description, votes = 0)
		charity_object.save()
	return render(request, 'webapp/charitieslist.html', {'charities':Charity.objects.all()})

def index(request):
	return HttpResponse("Hello, world. You're at charities.")

def new_charity_form(request):
	return render(request, 'webapp/new_charities_form.html')

def charity_vote(request):
	if request.method == 'POST': 
		id = request.POST.get("charity_id")
		charity_object = Charity.objects.get(pk=id)
		charity_object.votes += 1
		charity_object.save()
	return render(request, 'webapp/charitieslist.html', {'charities':Charity.objects.all()})
