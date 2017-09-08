from django.shortcuts import render
from users.models import User

# Create your views here.
def index(request):
    return render(request, 'users/index.html')

def list(request):
    users_list = User.objects.order_by('first_name')
    ctx = {'users_list': users_list}
    return render(request, 'users/list.html', context=ctx)
