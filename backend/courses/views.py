from rest_framework import viewsets, status
from rest_framework.permissions import BasePermission, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers_progress import ProgressSerializer

from django.shortcuts import render

from .models import Course, Video, Question, QuizResult
from .serializers import (
    CourseSerializer,
    VideoSerializer,
    QuizResultSerializer
)


# ------------------------- PAGE RENDER -------------------------
def course_list_page(request):
    courses = Course.objects.all().order_by("-created_at")
    return render(request, "student_courses.html", {"courses": courses})


# ------------------------- PERMISSION -------------------------
class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        if request.method in ["POST", "PUT", "PATCH", "DELETE"]:
            return getattr(request.user, "role", "") == "admin"
        return True  # allow GET for all


# ------------------------- COURSE VIEWSET -------------------------
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by("-created_at")
    serializer_class = CourseSerializer
    permission_classes = [AllowAny, IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


# ------------------------- VIDEO VIEWSET -------------------------
class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by("-created_at")
    serializer_class = VideoSerializer
    permission_classes = [AllowAny, IsAdminUser]


# ------------------------- SAVE QUESTIONS (ADMIN) -------------------------
class SaveQuestionsView(APIView):
    def post(self, request, course_id):
        questions = request.data.get("questions", [])

        # delete old questions
        Question.objects.filter(course_id=course_id).delete()

        # insert new
        for q in questions:
            Question.objects.create(
                course_id=course_id,
                question_text=q["question_text"],
                option_a=q["option_a"],
                option_b=q["option_b"],
                option_c=q["option_c"],
                option_d=q["option_d"],
                correct_answer=q["correct_answer"]
            )

        return Response({"message": "Saved"}, status=status.HTTP_200_OK)


# ------------------------- GET QUESTIONS (STUDENT) -------------------------
class CourseQuestionsView(APIView):

    def get(self, request, course_id):
        questions = Question.objects.filter(course_id=course_id)

        formatted = []
        for q in questions:
            formatted.append({
                "id": q.id,
                "question": q.question_text,
                "option_a": q.option_a,
                "option_b": q.option_b,
                "option_c": q.option_c,
                "option_d": q.option_d,
                # admin sees correct answer, students DON’T
                "correct_option": q.correct_answer if getattr(request.user, "role", "") == "admin" else None
            })

        return Response({"questions": formatted}, status=200)


# ------------------------- SAVE QUIZ RESULT (STUDENT) -------------------------
class SaveQuizResultView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, course_id):
        data = request.data
        data["student"] = request.user.id
        data["course"] = course_id

        serializer = QuizResultSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Quiz result saved"}, status=201)

        return Response(serializer.errors, status=400)
class GetProgressView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, course_id):
        progress, _ = CourseProgress.objects.get_or_create(
            student=request.user,
            course_id=course_id
        )
        return Response(CourseProgressSerializer(progress).data)
class CompleteModuleView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, course_id, module_index):
        progress, _ = CourseProgress.objects.get_or_create(
            student=request.user,
            course_id=course_id
        )

        if module_index not in progress.completed_modules:
            progress.completed_modules.append(module_index)
            progress.save()

        return Response({"message": "Module marked complete"})
class SaveQuizToProgressView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, course_id):
        score = request.data.get("score", 0)
        total = request.data.get("total", 0)

        progress, _ = CourseProgress.objects.get_or_create(
            student=request.user,
            course_id=course_id
        )

        progress.quiz_score = score
        progress.quiz_total = total
        progress.save()

        return Response({"message": "Quiz saved to progress"})
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Progress
from .serializers_progress import ProgressSerializer


class GetProgressView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, course_id):
        progress, created = Progress.objects.get_or_create(
            student=request.user,
            course_id=course_id,
        )
        serializer = ProgressSerializer(progress)
        return Response(serializer.data, status=200)


class UpdateProgressView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, course_id):
        completed = request.data.get("completed", [])

        progress, created = Progress.objects.get_or_create(
            student=request.user,
            course_id=course_id,
        )

        progress.completed = completed
        progress.save()

        return Response({"message": "Progress updated"}, status=200)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Progress
from django.contrib.auth import get_user_model

User = get_user_model()


class CompleteModuleView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, course_id, module_index):
        user = request.user

        progress, created = Progress.objects.get_or_create(
            student=user,
            course_id=course_id
        )

        passed = progress.modules_passed
        if module_index not in passed:
            passed.append(module_index)
            progress.modules_passed = passed
            progress.save()

        return Response(
            {"message": "Module marked complete", "modules_passed": passed},
            status=status.HTTP_200_OK
        )
