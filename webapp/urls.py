from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.my_profile, name='my_profile'),
    url(r'^donations', views.zuora_profile, name='zuora_profile'),
    url(r'charities/new', views.new_charity, name='new_charity'),
    url(r'charities/vote', views.charity_vote, name='charity_vote'),
    url(r'charities', views.show_charities, name='show_charities'),
]
