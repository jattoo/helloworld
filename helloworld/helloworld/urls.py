from django.contrib import admin
from django.urls import path
from helloapp import endpoints
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(endpoints)),
]
