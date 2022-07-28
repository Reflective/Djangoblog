from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Jungle Wizard',
        'title': 'Welcome to the Jungle',
        'content': 'First post content',
        'date_posted': 'July 27, 2022'         
    },    
    {
        'author': 'Stinkman',
        'title': 'I am sad',
        'content': 'Deuces content',
        'date_posted': 'July 28, 2022'         
    },
    
]



# Create your views here. 
def home(request):
    context = {
        'posts': posts
    }
    
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html', {'title': 'About'})