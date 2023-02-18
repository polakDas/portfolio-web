from rest_framework import serializers

from ..models import Diary


class DiaryListSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(
    #     view_name="api:detail"
    # )
    class Meta:
        model = Diary
        fields = ("title", "details", "created_at", "updated_at", "url")

        extra_kwargs = {"url": {"view_name": "api:diary-detail", "lookup_field": "pk"}}


class DiaryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ("title", "details", "created_at", "updated_at")
