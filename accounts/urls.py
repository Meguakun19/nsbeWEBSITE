# List of URLs just for the accounts section
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),


]