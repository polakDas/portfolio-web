# flake8: noqa
from django.shortcuts import render
from rest_framework import generics

from .models import Diary
from .serializers import DiarySerializer


# Create your views here.
class DiaryAPIList(generics.ListCreateAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer


class DiaryAPIDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
