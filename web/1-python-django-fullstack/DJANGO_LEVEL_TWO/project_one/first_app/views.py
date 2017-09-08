from django.shortcuts import render
from first_app.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    ctx = {'access_records': webpages_list}
    return render(request, 'first_app/index.html', context=ctx)
