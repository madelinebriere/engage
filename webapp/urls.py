from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'charities', views.show_charities, name='show_charities'),
    url(r'charities/new', views.new_charity, name='new_charity'),
    url(r'charities/vote', views.charity_vote, name='charity_vote'),
    url(r'profile', views.profile, name='profile'),
]
