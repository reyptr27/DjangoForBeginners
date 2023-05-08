from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import post
from django.urls import reverse_lazy

# Create your views here.

class BlogListView(ListView):
    model = post
    template_name = "blog/blog.html"

class BlogDetailView(DetailView):
    model = post
    template_name = "blog/blog_detail.html"

class BlogCreateView(CreateView):
    model = post
    fields = ['title', 'author', 'content']
    template_name = "blog/blog_add.html"
    success_url = reverse_lazy("blogpage")

class BlogUpdateView(UpdateView):
    model = post
    fields = ['title', 'content']
    template_name = "blog/blog_edit.html"
    success_url = reverse_lazy("blogpage")
    
class BlogDeleteView(DeleteView):
    model = post
    template_name = "blog/blog_delete.html"
    success_url = reverse_lazy("blogpage")