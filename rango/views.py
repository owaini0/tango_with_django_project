from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World, Rango <a href="/rango/about">About Page</a> ')

def about(request):
    return HttpResponse('Rango says here is the about page, to go back to index <a href="/rango">click here</a>')