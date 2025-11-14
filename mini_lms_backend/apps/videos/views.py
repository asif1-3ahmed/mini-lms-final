from rest_framework import viewsets, permissions
from .models import Video
from .serializers import VideoSerializer

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS: return True
        return request.user.is_authenticated and request.user.role == "ADMIN"

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by("-created_at")
    serializer_class = VideoSerializer
    permission_classes = [IsAdminOrReadOnly]
