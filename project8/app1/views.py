from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def string1(request):
    return HttpResponse('prasanna')

def string(request):
    return HttpResponse('radha')