from django.contrib import admin
from django.urls import path
from django.urls.conf import include

# Colocando a urls.API no sistema
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    
]
