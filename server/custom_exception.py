from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
import json.decoder

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, json.decoder.JSONDecodeError):
        return Response(
            {"error": "Invalid JSON format. Please send valid JSON."},
            status=status.HTTP_400_BAD_REQUEST
        )

    if response is not None and response.status_code == 400:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        response.data = {
            "errors": response.data
        }

    return response