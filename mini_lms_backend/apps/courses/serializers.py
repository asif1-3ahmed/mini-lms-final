from rest_framework import serializers
from .models import Course, Category, Enrollment
from apps.videos.serializers import VideoSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id","name","slug")

class CourseSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.id")
    videos = VideoSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ("id","title","description","category","owner","is_published","created_at","videos")
