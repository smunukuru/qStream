import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render
import json


# Create your views here.


def home(request):
    return HttpResponse('This is home page!! The current date time is ' + str(datetime.datetime.now()))


def my_test(request):
    userdata = '{"data":{"type":"users", "attributes":{"first_name":"Foo","last_name":"Bar","email_address":"baz@qux.com","country":"Ireland"}}}'
    #y = json.loads(userdata)
    #return HttpResponse(y['data']['attributes']['first_name'])
    return HttpResponse(userdata)



def good_morning(request):
    return HttpResponse('Good Morning')


def good_afternoon(request):
    return HttpResponse('Good Afternoon!!!')


def org_chart(request):
    return render(request, 'qstreamtest/Orgchart.html', {'title1': 'Org', 'title2': 'Chart!!'})
