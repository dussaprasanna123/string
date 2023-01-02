from django.urls import path
from app1.views import *
app_name='vamsi'
urlpatterns=[
    path('vamsi/',vamsi,name='vamsi'),
]