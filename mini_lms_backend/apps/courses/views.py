from rest_framework import viewsets, permissions
from .models import Course
from .serializers import CourseSerializer
from .permissions import IsAdminCreateAndOwnerEdit

class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    permission_classes = [IsAdminCreateAndOwnerEdit]

    def get_queryset(self):
        user = self.request.user
        qs = Course.objects.select_related("owner").all()
        if user.is_authenticated and user.role == "ADMIN":
            return qs.filter(owner=user)  # admin sees only their courses
        return qs.filter(is_published=True)  # students/public see published courses

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
