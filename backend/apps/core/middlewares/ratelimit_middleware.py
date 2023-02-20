from ipware import get_client_ip


def ParseClientIpMiddleware(get_response):
    def middleware(request):
        request.META["REMOTE_ADDR"] = get_client_ip(request)[0]
        response = get_response(request)
        return response

    return middleware


from django.conf import settings
from django.utils.module_loading import import_string

from django_ratelimit.exceptions import Ratelimited


class RatelimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        if not isinstance(exception, Ratelimited):
            return None
        view = import_string(settings.RATELIMIT_VIEW)
        return view(request, exception)
