from rest_framework import viewsets, permissions
from .models import Course
from .serializers import CourseSerializer

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS: return True
        return request.user.is_authenticated and request.user.role == "ADMIN"

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by("-created_at")
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrReadOnly]
