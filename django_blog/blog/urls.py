from django.urls import path
from . import views
#Connects urls to apps as defined in views.py
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
