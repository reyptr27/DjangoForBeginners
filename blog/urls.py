from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path("", BlogListView.as_view(), name="blogpage"),
    path("<int:pk>/", BlogDetailView.as_view(), name="blogpage_detail"),
    path("add/", BlogCreateView.as_view(), name="blogpage_add"),
    path("<int:pk>/edit/", BlogUpdateView.as_view(), name="blogpage_edit"),
    path("<int:pk>/delete/", BlogDeleteView.as_view(), name="blogpage_delete")
]