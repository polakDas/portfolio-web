from rest_framework import serializers

from .models import Diary


class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ("title", "details", "created_at", "updated_at")
