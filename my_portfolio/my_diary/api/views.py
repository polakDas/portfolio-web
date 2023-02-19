from django.shortcuts import render  # noqa F401
from rest_framework import generics
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from ..models import Diary
from .serializers import DiaryDetailSerializer, DiaryListSerializer


# Create your views here.
class DiaryViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):
    serializer_class = DiaryListSerializer
    queryset = Diary.objects.order_by("created_at")
    # lookup_field = "pk"


class DiaryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Diary.objects.order_by("created_at")
    serializer_class = DiaryListSerializer


class DiaryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Diary.objects.order_by("created_at")
    serializer_class = DiaryDetailSerializer
