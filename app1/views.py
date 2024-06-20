from django.shortcuts import render
from  django.http import HttpResponse

# Create your views here.
def function1(request):
    return HttpResponse("Function is created in views")
      