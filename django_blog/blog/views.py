from django.shortcuts import render
from django.views.generic import ListView 
from .models import Post

#homepage
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    
    return render(request, 'blog/home.html', context)

#Class based view
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

#Function based view
def about(request):
    return render(request,'blog/about.html', {'title': 'About'})


