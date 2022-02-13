from django.urls import path

from . import views

urlpatterns = [
    path("get-wav", views.GetWav.as_view(), name="get-wav"),
    path("get-spec", views.GetSpec.as_view(), name="get-spec"),
]
