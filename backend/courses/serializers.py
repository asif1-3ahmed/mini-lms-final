from rest_framework import serializers
from .models import Course, Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"
        read_only_fields = ("id", "created_at")


class CourseSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ("id", "title", "description", "category", "created_by", "created_at", "videos")
        read_only_fields = ("id", "created_by", "created_at", "videos")
