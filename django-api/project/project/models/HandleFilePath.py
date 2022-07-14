from django.conf import settings
from urllib.parse import urlparse, urlunparse

#This supports the absolute url if no request is set! For example asgi

class HandleFilePath:

    @staticmethod
    def build_absolute_uri(obj_url):
        base_url = "http://" + settings.FILEPATH_HOST
        url_parts = list(urlparse(base_url))
        url_parts[2] = obj_url
        return urlunparse(url_parts)