from django.conf.urls import url
from . import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/', views.profile, name='profile')
]