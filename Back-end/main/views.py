from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def teachers(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())