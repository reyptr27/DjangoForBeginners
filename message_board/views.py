from django.views.generic import ListView
from .models import post

# Create your views here.

class PostListView(ListView):
    model = post
    template_name = "message_board/post.html"