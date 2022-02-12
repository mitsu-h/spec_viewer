from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
import librosa
import tempfile


class GetWav(APIView):
    def get(self, request, format=None):
        return Response({"message": "音声ファイルをPOSTして下さい"}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """音声ファイルから、波形のデータとサンプリングレートを獲得する

        Args:
            request (dict[_io.BufferedReader]): ファイルオブジェクト
            format ([type],  optional): [description]. Defaults to None.

        Returns:
            [dict[numpy.ndarray, int]]: 波形の配列と、サンプリングレート
        """
        request_data = request.data
        fp = tempfile.NamedTemporaryFile()
        fp.write(request_data["file"].read())
        fp.seek(0)
        # wav, fs = librosa.load(io.BytesIO(request_data["file"].read()), sr=None)
        wav, fs = librosa.load(fp.name, sr=None)
        return Response({"wav": wav, "fs": fs}, status=status.HTTP_200_OK)
