from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'charities', views.charitiesList, name='charitiesList'),
    url(r'^$', views.home, name='home'),
    url(r'dashboard', views.dashboard, name='dashboard'),
]
