from django.shortcuts import render
from django.shortcuts import HttpResponse

def hello_world(request):
    return HttpResponse(content='Hello world')



