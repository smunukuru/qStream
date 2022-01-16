from django.urls import path
from qstreamtest import views
from qstreamtest.views import home, my_test, good_morning, good_afternoon, org_chart

urlpatterns = [
    path('', home),
    path('empapi/', my_test),
    path('morning/', good_morning),
    path('afternoon/', good_afternoon),
    path('orgchart/', org_chart),
]
