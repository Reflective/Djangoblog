from django.urls import path
from.views import PostListView
from . import views
#Connects urls to apps as defined in views.py
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
