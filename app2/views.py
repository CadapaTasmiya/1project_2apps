from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def function2(request):
    return HttpResponse('function in app2 created successfully')