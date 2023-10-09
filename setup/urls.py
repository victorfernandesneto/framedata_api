from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('capcom/', admin.site.urls),
    path('', include('apps.framedata.urls')),
]
