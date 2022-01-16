from django.http import HttpResponse


class HttpResponseMixin(object):
    def render_to_http_response(self, jason_data):
        # 1000 lines of code can be written here before
        return HttpResponse(jason_data, content_type="application/jason")
