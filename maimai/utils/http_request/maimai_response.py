from rest_framework import status
from rest_framework.response import Response


class MaimaiResponse(Response):
    def __init__(self, data=None, status_code=None, template_name=None, headers=None, exception=False, content_type=None):
        if status_code is None:
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        elif status_code <= 200:
            status_code = status.HTTP_200_OK
        super().__init__(data, status_code, template_name, headers, exception, content_type)
