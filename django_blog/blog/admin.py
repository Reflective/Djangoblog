from django.contrib import admin
from .models import Post

admin.site.register(Post)  # Allows model to be accessed from admin site
