from django.urls import path
from arthimetic import views

urlpatterns = [
        path('add/', views.add),
        path('getex/add1', views.add1),
        path('getex/', views.getexample),
        path('sub/', views.substract),
        path('home/', views.hometmpl),
        path('about/', views.abttmpl),
        path('emp/', views.employee),
]