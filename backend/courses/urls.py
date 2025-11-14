from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, VideoViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r"courses", CourseViewSet, basename="course")
router.register(r"videos", VideoViewSet, basename="video")

urlpatterns = [
    path("", include(router.urls)),
]
