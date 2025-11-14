from rest_framework import viewsets, permissions
from .models import Quiz, Question
from .serializers import QuizSerializer, QuestionSerializer


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return getattr(request.user, "role", "") == "admin"


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = (permissions.IsAuthenticated, IsAdminOrReadOnly)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAuthenticated, IsAdminOrReadOnly)
