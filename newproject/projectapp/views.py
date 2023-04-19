from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from . models import People
from . models import Site
# Create your views here.
def demo(request):
    obj=Site.objects.all()
    return render(request,"index.html",{'result':obj})
def people(request):
    name=People.objects.all()
    return render(request,"index.html",{'final':name})
