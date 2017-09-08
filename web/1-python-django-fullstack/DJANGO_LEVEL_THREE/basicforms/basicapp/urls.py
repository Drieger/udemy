from django.conf.urls import url
from basicapp import views

urlpatterns = [
    url(r'^$', views.form, name='form'),
    url(r'^user-form/', views.modelform, name='userform'),
]
