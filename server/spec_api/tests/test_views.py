from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase
import os
import librosa
import numpy as np


# Create your tests here.
class GetWavTest(APITestCase):
    def test_get(self):
        url = reverse("get-wav")
        response = self.client.get(url)
        self.assertAlmostEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "音声ファイルをPOSTして下さい")

    def test_wav_format(self):
        url = reverse("get-wav")
        wav_path = os.path.join(os.path.dirname(__file__), "audio/compare.wav")
        response = self.client.post(url, {"file": open(wav_path, "rb")})
        wav, fs = librosa.load(wav_path, sr=None)
        self.assertEqual((response.data["wav"] == wav).all(), True)
        self.assertEqual(response.data["fs"], fs)

    def test_m4a_format(self):
        url = reverse("get-wav")
        wav_path = os.path.join(os.path.dirname(__file__), "audio/st_mode_gl.m4a")
        response = self.client.post(url, {"file": open(wav_path, "rb")})
        wav, fs = librosa.load(wav_path, sr=None)
        self.assertEqual((response.data["wav"] == wav).all(), True)
        self.assertEqual(response.data["fs"], fs)

    def test_aifc_format(self):
        url = reverse("get-wav")
        wav_path = os.path.join(os.path.dirname(__file__), "audio/枯葉20201016.aifc")
        response = self.client.post(url, {"file": open(wav_path, "rb")})
        wav, fs = librosa.load(wav_path, sr=None)
        self.assertEqual((response.data["wav"] == wav).all(), True)
        self.assertEqual(response.data["fs"], fs)


class GetSpecTest(APITestCase):
    def test_normal(self):
        url = reverse("get-spec")
        wav_path = os.path.join(os.path.dirname(__file__), "audio/compare.wav")
        wav, fs = librosa.load(wav_path, sr=None)
        n_fft = 2048
        response = self.client.post(url, {"wav": wav, "n_fft": n_fft}, format="json")

        stft = np.abs(librosa.stft(wav, n_fft=n_fft))
        self.assertAlmostEqual((response.data["wav"] == wav).all(), True)
        self.assertEqual((response.data["spec"] == stft).all(), True)

