from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def jyo(request,name):
    return HttpResponse(f'Happy sankranthi     {name}')