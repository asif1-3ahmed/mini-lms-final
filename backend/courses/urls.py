from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, VideoViewSet, course_list_api, course_list_page, course_single_api  # ✅ import here

router = DefaultRouter()
router.register(r"courses", CourseViewSet, basename="course")
router.register(r"videos", VideoViewSet, basename="video")

urlpatterns = [
    path("api/", include(router.urls)),               # /api/courses/, /api/courses/<id>/, /api/videos/
    path("api/public/courses/", course_list_api, name="public-course-list"),
    path("admin/manage-courses/", course_list_page, name="admin-manage-courses-page"),

]
