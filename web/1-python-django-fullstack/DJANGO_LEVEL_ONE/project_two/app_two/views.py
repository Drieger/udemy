from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<em>Hello World!</em>')

def help(request):
    return render(request, 'help.html')
