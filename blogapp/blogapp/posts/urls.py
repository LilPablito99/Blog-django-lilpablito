from django.contrib import admin
from django.urls import path, include
from perfiles.views import SignUpView, BienvenidaView,SignInView,SignOutView
from . import views
urlpatterns = [
    path('Crear_post/',views.PostCreateView.as_view(), name='add_post'),
   
    
]