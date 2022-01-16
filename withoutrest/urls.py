from django.urls import path
from withoutrest import views

urlpatterns = [
        path('', views.home),
        path('html_empapi/', views.emp_data_view),
        path('json_empapi/', views.emp_data_jview),
        path('offers/', views.special_offers),
        path('cbvapi/', views.JsonCBV.as_view()),
]