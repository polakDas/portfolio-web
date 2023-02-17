# flake8: noqa
from django.urls import path

from .views import DiaryAPIDetails, DiaryAPIList

app_name = "my_diary"

urlpatterns = [
    path("", DiaryAPIList.as_view(), name="diary-list"),
    path("<int:pk>/", DiaryAPIDetails.as_view(), name="diary-detail"),
]
