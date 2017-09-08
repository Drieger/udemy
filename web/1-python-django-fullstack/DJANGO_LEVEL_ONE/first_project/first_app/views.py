from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def render_to(template):
    def func_wrapper(view):
        def wrapper(request, *args, **kwargs):
            return render(request, template, view(request))
        return wrapper
    return func_wrapper

def index(request):
    my_dict = { 'insert_me': 'I\'ve been inserted' }
    return render(request, 'first_app/index.html', context=my_dict)

@render_to('first_app/decorated.html')
def decorated(request):
    return {'insert': 'I\'m decorated'}
