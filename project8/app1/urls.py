from django.urls import path
from app1.views import *
app1_name='something'
urlpatterns=[
    path('string1/',string1,name='string1'),
    path('string/',string,name='string')

]