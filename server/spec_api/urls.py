from django.urls import URLPattern, path

from . import views

urlpatterns = [
    path('', views.HelloWorld.as_view(), name='hello')
]