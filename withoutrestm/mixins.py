from django.core.serializers import serialize
import json

from django.http import HttpResponse


class SerializeMixin(object):
    def serialize(self, qs):
        json_data = serialize('json', qs)
        list_dict = json.loads(json_data)
        final_list = []
        for obj in list_dict:
            final_list.append(obj['fields'])
        json_data = json.dumps(final_list)
        # print('its me mixin serialize')
        return json_data


class HttpRenderMixin(object):
    def http_response_data_render(self, json_data, status=200):
        # print('its me mixin http response1')
        return HttpResponse(json_data, content_type='application/json', status=status)
