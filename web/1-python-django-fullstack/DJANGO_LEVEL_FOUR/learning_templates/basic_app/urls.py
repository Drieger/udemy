from django.conf.urls import url
from . import views

app_name = 'basic-app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^second/$', views.second, name='second')
]
