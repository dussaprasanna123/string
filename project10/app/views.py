from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request,'hello.html')

def hi(request):
    return render(request,'hi.html')