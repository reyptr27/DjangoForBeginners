from django.urls import path
from .views import BlogListView, BlogDetailView

urlpatterns = [
    path("", BlogListView.as_view(), name="blogpage"),
    path("<int:pk>/", BlogDetailView.as_view(), name="blogpage_detail")
]