# Create your views here.
import json

from django.utils.decorators import method_decorator
from django.views import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from requests import post

from withoutrestm.forms import EmployeeForm
from withoutrestm.mixins import SerializeMixin, HttpRenderMixin
from withoutrestm.models import Employee
from withoutrestm.utils import is_valid_data


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeCRUDCBV(HttpRenderMixin, SerializeMixin, View):
    def get_object_by_id(self, id):
        try:
            emp_details = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp_details = None
        return emp_details

    def get(self, request, *args, **kwargs):
        input_data_json = request.body
        if not is_valid_data(input_data_json):
            json_data = json.dumps({'msg': 'Input data is not a valid jsonn'})
            return self.http_response_data_render(json_data, status=400)
        dict_input_data = json.loads(input_data_json)
        id = dict_input_data.get('id', None)
        if id is not None:
            emp_details = self.get_object_by_id(id)
            if emp_details is None:
                json_data = json.dumps({'msg': 'The matched resource is not available', 'status': 404})
                return self.http_response_data_render(json_data, status=404)
            json_data = self.serialize([emp_details, ])
            return self.http_response_data_render(json_data)
        qs = Employee.objects.all()
        json_data = self.serialize(qs)
        return self.http_response_data_render(json_data)

    def post(self, request, *args, **kwargs):
        data = request.body
        if not is_valid_data(data):
            json_data = json.dumps({'msg': 'Data is not a valid json'})
            return self.http_response_data_render(json_data, status=400)
        emp_data = json.loads(data)
        form = EmployeeForm(emp_data)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'Resource created successfully'})
            return self.http_response_data_render(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.http_response_data_render(json_data, status=400)

    def put(self, request, *args, **kwargs):
        input_data_json = request.body
        if not is_valid_data(input_data_json):
            json_data = json.dumps({'msg': 'Input data is not a valid jsonn'})
            return self.http_response_data_render(json_data, status=400)
        input_data_dict = json.loads(input_data_json)
        id = input_data_dict.get('id', None)
        if id is not None:
            emp_details = self.get_object_by_id(id)
            if emp_details is None:
                json_data = json.dumps(
                    {'msg': 'The matched resource is not available. Not able to update', 'status': 404})
                return self.http_response_data_render(json_data, status=404)
        json_data_orig = self.serialize([emp_details, ])
        dict_data_orig = json.loads(json_data_orig)
        for obj in dict_data_orig:
            obj.update(input_data_dict)
            form = EmployeeForm(obj, instance=emp_details)
            if form.is_valid():
                form.save(commit=True)
                json_data = json.dumps({'msg': 'Resource updated successfully'})
                return self.http_response_data_render(json_data)
            if form.errors:
                json_data = json.dumps(form.errors)
                return self.http_response_data_render(json_data, status=400)

    def delete(self, request, *args, **kwargs):
        input_data_json = request.body
        if not is_valid_data(input_data_json):
            json_data = json.dumps({'msg': 'Input data is not a valid jsonn'})
            return self.http_response_data_render(json_data, status=400)
        dict_input_data = json.loads(input_data_json)
        id = dict_input_data.get('id', None)
        if id is not None:
            emp_details = self.get_object_by_id(id)
            if emp_details is None:
                json_data = json.dumps({'msg': 'The matched resource is not available', 'status': 404})
                return self.http_response_data_render(json_data, status=404)
            status, deleted_item = emp_details.delete()
            if status == 1:
                json_data = json.dumps({'msg': 'Resource deleted successfully'})
                return self.http_response_data_render(json_data)
            else:
                json_data = json.dumps({'msg': 'Resource unable to delete'})
                return self.http_response_data_render(json_data, status=400)

        json_data = json.dumps({'msg': 'To delete id is required'})
        return self.http_response_data_render(json_data, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeDetails(HttpRenderMixin, SerializeMixin, View):
    def get_object_by_id(self, id):
        try:
            emp_details = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp_details = None
        return emp_details

    def get(self, request, id, *args, **kwargs):
        try:
            emp_details = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data = json.dumps({'msg': 'The requested resource is not available ', 'status': 404})
            return self.http_response_data_render(json_data, status=404)
        else:
            json_data = self.serialize([emp_details, ])
            return self.http_response_data_render(json_data)

    def put(self, request, id, *args, **kwargs):
        emp_details = self.get_object_by_id(id)
        if emp_details is None:
            json_data = json.dumps({'msg': 'The matched resource is not available', 'status': 404})
            return self.http_response_data_render(json_data, status=404)
        json_data_orig = self.serialize([emp_details, ])
        dict_data_orig = json.loads(json_data_orig)
        input_data_json = request.body
        if not is_valid_data(input_data_json):
            json_data = json.dumps({'msg': 'Input data is not a valid json'})
            return self.http_response_data_render(json_data, status=400)
        input_data_dict = json.loads(input_data_json)
        for obj in dict_data_orig:
            obj.update(input_data_dict)
            form = EmployeeForm(obj, instance=emp_details)
            if form.is_valid():
                form.save(commit=True)
                json_data = json.dumps({'msg': 'Resource updated successfully'})
                return self.http_response_data_render(json_data)
            if form.errors:
                json_data = json.dumps(form.errors)
                return self.http_response_data_render(json_data, status=400)

    def delete(self, request, id, *args, **kwargs):
        emp_details = self.get_object_by_id(id)
        if emp_details is None:
            json_data = json.dumps({'msg': 'The matched resource is not available', 'status': 404})
            return self.http_response_data_render(json_data, status=404)
        status, deleted_item = emp_details.delete()
        if status == 1:
            json_data = json.dumps({'msg': 'Resource deleted successfully'})
            return self.http_response_data_render(json_data)
        else:
            json_data = json.dumps({'msg': 'Resource unable to delete'})
            return self.http_response_data_render(json_data, status=400)

        #
        # to exempt from the csrf you will need to import 'csrf_exempt' from django.views.decorators.cfrf
        #


@method_decorator(csrf_exempt, name='dispatch')
class AllEmployeeDetails(HttpRenderMixin, SerializeMixin, View):
    def get(self, request, *args, **kwargs):
        qs = Employee.objects.all()
        json_data = self.serialize(qs)
        return HttpResponse(json_data, content_type="application/json")

    def post(self, request, *args, **kwargs):
        data = request.body
        if not is_valid_data(data):
            json_data = json.dumps({'msg': 'Data is not a valid json'})
            return self.http_response_data_render(json_data, status=400)
        emp_data = json.loads(data)
        form = EmployeeForm(emp_data)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'Resource created successfully'})
            return self.http_response_data_render(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.http_response_data_render(json_data, status=400)
