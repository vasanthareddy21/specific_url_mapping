from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<h1>first string</h1>')

def second(request):
    return HttpResponse('<h1> second string</h1>')
