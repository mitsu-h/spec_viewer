from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status
import librosa
import io

# Create your views here.
class HelloWorld(APIView):
    """
    クラスベースのAPIView
    ・HTTPのメソッドがクラスのメソッドになるので、わかりやすい
    """

    def get(self, request, format=None):
        return Response({"message": "Hello World!!"}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        request_data = request.data
        return Response(
            {"message": request_data["message"]}, status=status.HTTP_201_CREATED
        )


class GetWav(APIView):
    """
    """

    def get(self, request, format=None):
        return Response({"message": "音声ファイルをPOSTして下さい"}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        request_data = request.data
        wav, fs = librosa.load(io.BytesIO(request_data["file"].read()), sr=None)
        return Response({"wav": wav, "fs": fs}, status=status.HTTP_200_OK)
