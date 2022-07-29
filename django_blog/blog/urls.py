from django.urls import path
from.views import PostListView, PostDetailView
from . import views
#Connects urls to apps as defined in views.py
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='blog-about')
]
