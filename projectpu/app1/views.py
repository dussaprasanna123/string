from django.shortcuts import render

# Create your views here.
def pooji(request):
    return render(request,'pooji.html')

def ajju(request):
    return render(request,'ajju.html')