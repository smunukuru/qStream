from django.conf.urls import url
from django.urls import path
from withoutrestm import views

urlpatterns = [

        # url(r'^empapi/(?P<id>\d+)/$', views.EmployeeDetails.as_view()),
        # url(r'^empapi/', views.AllEmployeeDetails.as_view()),
        url(r'^empapi/', views.EmployeeCRUDCBV.as_view()),
]