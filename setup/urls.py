from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('capcom/', admin.site.urls),
    path('', include('apps.framedata.urls')),
]
