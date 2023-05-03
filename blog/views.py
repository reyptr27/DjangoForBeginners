from django.views.generic import ListView, DetailView
from .models import post

# Create your views here.

class BlogListView(ListView):
    model = post
    template_name = "blog/blog.html"

class BlogDetailView(DetailView):
    model = post
    template_name = "blog/blog_detail.html"