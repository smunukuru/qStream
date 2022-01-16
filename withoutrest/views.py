import json

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import View

from bakery.models import SpecialOffers
from withoutrest.mixins import HttpResponseMixin


def home(request):
    return HttpResponse('This is django rest api  home page')


def emp_data_view(request):
    emp_date = {
        'eno': 100,
        'ename': 'Sunny',
        'esal': 1000,
        'eaddr': 'Hyderabad'

    }
    resp = 'Employee Number: {}<br>Employee Name: {}<br> Employee Salary: {}<br> Employee Address: {}<br>'.format(
        emp_date['eno'],
        emp_date['ename'],
        emp_date['esal'],
        emp_date['eaddr'])
    return HttpResponse(resp)


def emp_data_jview(request):
    emp_date = {

        'data': {

            'type': 'users',
            'attributes': [
                {"first_name": "Foo1",
                 "last_name": "Bar1",
                 "email_address": "baz1@qux.com",
                 "country": "Ireland"
                 },
                {"first_name": "Foo2",
                 "last_name": "Bar2",
                 "email_address": "baz2@qux.com",
                 "country": "UK"
                 },
                {"first_name": "Foo3",
                 "last_name": "Bar3",
                 "email_address": "baz3@qux.com",
                 "country": "USA"
                 }

            ]
        }

    }
    # json_data = json.dumps(emp_date)
    # return HttpResponse(json_data, content_type='application/json')

    return JsonResponse(emp_date)


def special_offers(request):
    data = serializers.serialize('json', SpecialOffers.objects.all())
    # json_data = json.loads(data)
    return HttpResponse(data, content_type='application/json')


class JsonCBV(HttpResponseMixin, View):
    def get(self, request, *args, **kwargs):
        emp_date = {'msg': 'this is from get method'}
        return self.render_to_http_response(json.dumps(emp_date))

    def post(self, request, *args, **kwargs):
        emp_date = {'msg': 'this is from post method'}
        return self.render_to_http_response(json.dumps(emp_date))

    def put(self, request, *args, **kwargs):
        emp_date = {'msg': 'this is from put method'}
        return self.render_to_http_response(json.dumps(emp_date))

    def delete(self, request, *args, **kwargs):
        emp_date = {'msg': 'this is from delete method'}
        return self.render_to_http_response(json.dumps(emp_date))
