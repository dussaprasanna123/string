from django.urls import path
from app1.views import *
app_name='allu'
urlpatterns=[
    path('pooji/',pooji,name='pooji'),
    path('ajju/',ajju,name='ajju'),
]