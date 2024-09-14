# from .views import *
# from django.urls import path
# urlpatterns=[
# path('set',set,name='set'),
# path("get",get,name='get'),
# ]
from django.contrib import admin
from django.urls import path,include
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('set/', set, name='set'),
    path('get/', get, name='get'),
    # path('',include ('myapp.urls'))
]