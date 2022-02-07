from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status

# Create your views here.
class HelloWorld(APIView):
    """
    クラスベースのAPIView
    ・HTTPのメソッドがクラスのメソッドになるので、わかりやすい
    """
    def get(self, request, format=None):
        return Response({"message": "Hello World!!"},
            status=status.HTTP_200_OK)

    def post(self, request, format=None):
        request_data = request.data
        return Response({"message": request_data["message"]},
            status=status.HTTP_201_CREATED)