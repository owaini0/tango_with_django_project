from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context_dict)

def about(request):
    tutorial_credit = {'name': 'Mansoor'}
    return render(request, 'rango/about.html', tutorial_credit)