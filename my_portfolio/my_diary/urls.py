# flake8: noqa
from django.urls import path
from django.views.generic.base import RedirectView

from .api.views import DiaryListCreateAPIView, DiaryRetrieveUpdateDestroyAPIView

app_name = "my_diary"

urlpatterns = [
    path("", RedirectView.as_view(url="list/", permanent=False)),
    path("list/", DiaryListCreateAPIView.as_view(), name="list"),
    path("<int:pk>/", DiaryRetrieveUpdateDestroyAPIView.as_view(), name="detail"),
]
