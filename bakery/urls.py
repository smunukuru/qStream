from django.urls import path
from bakery import views

urlpatterns = [
        path("", views.home),
]