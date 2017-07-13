from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'charities', views.charitiesList, name='charitiesList'),
    url(r'charities/new', views.new_charity_form, name='new_charity_form')
    url(r'^$', views.index, name='index'),
    url(r'dashboard', views.dashboard, name='dashboard'),
]
