from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'charities', views.charitiesList, name='charitiesList'),
    url(r'^$', views.index, name='index'),
]