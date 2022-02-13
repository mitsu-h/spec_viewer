import pdb
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
import librosa
import tempfile
import numpy as np
import io


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
        file_bytes = request_data["file"].read()
        try:
            wav, fs = librosa.load(io.BytesIO(file_bytes), sr=None)
        except RuntimeError:
            fp = tempfile.NamedTemporaryFile()
            fp.write(file_bytes)
            fp.seek(0)
            wav, fs = librosa.load(fp.name, sr=None)
        return Response({"wav": wav, "fs": fs}, status=status.HTTP_200_OK)


class GetSpec(APIView):
    def get(self, request, format=None):
        return Response({"message": "音声波形をPOSTして下さい"}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """音声波形から、振幅スペクトログラムを返す

        Args:
            self (numpy.ndarray): 音声波形
            format ([type], optional): [description]. Defaults to None.

        Returns:
            numpy.ndarray: 振幅スペクトログラム
        """
        request_data = request.data
        spec = np.abs(
            librosa.stft(
                np.array(request_data["wav"], dtype=np.float32),
                n_fft=request_data["n_fft"],
            )
        )
        return Response(
            {"spec": spec, "wav": request_data["wav"]}, status=status.HTTP_200_OK
        )

