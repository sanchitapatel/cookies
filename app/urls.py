from .views import *
from django.urls import path
urlpatterns=[
path('set',set,name='set'),
path("get",get,name='get'),
]