from rest_framework import viewsets, permissions
from .models import Course, Video
from .serializers import CourseSerializer, VideoSerializer


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return getattr(request.user, "role", "") == "admin"


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by("-created_at")
    serializer_class = CourseSerializer
    permission_classes = (permissions.IsAuthenticated, IsAdminOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by("-created_at")
    serializer_class = VideoSerializer
    permission_classes = (permissions.IsAuthenticated, IsAdminOrReadOnly)
