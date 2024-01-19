from django.urls import re_path
from . import views

urlpatterns = [
    re_path('Login', views.Login),
    re_path('SingUp', views.SingUp),
    re_path('TestToken', views.TestToken),
    
]