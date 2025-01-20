from django.http import HttpRequest

def index(request):
    return HttpRequest('Rango says here is the about page')