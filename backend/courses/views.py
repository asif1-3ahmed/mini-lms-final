from rest_framework import viewsets
from rest_framework.permissions import BasePermission, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Course, Video
from .serializers import CourseSerializer, VideoSerializer

from django.shortcuts import render
from .models import Course

def course_list_page(request):
    courses = Course.objects.all().order_by("-created_at")
    return render(request, "student_courses.html", {"courses": courses})


# ✅ Only block modifications, allow GET for browser + React
class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        if request.method in ["POST", "PUT", "PATCH", "DELETE"]:
            return getattr(request.user, "role", "") == "admin"
        return True  # ✅ Allow GET for everyone (NO 401)

# ✅ Course Viewset should not require auth for reading
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by("-created_at")
    serializer_class = CourseSerializer
    permission_classes = [AllowAny, IsAdminUser]  # ✅ GET works without login

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by("-created_at")
    serializer_class = VideoSerializer
    permission_classes = [AllowAny, IsAdminUser]

# ✅ Simple API function for React to call
