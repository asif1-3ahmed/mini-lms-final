from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from courses.views import CourseViewSet, VideoViewSet

router = DefaultRouter()
router.register(r"courses", CourseViewSet, basename="course")
router.register(r"videos", VideoViewSet, basename="video")

urlpatterns = [
    path("admin/", admin.site.urls),

    # Main API
    path("api/", include(router.urls)),

    # Auth APIs
    path("api/auth/", include("accounts.urls")),

    # QUIZ URLS (student + admin)
    path("", include("courses.urls")),
]
