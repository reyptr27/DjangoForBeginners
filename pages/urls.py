from django.urls import path, include
from .views import HomePageView, AboutPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path("about/", AboutPageView.as_view(), name="aboutpage"),
]