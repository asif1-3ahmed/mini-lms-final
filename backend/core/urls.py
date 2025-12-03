from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from courses.views import CourseViewSet, VideoViewSet
from accounts.views import MyTokenObtainPairView, current_user  # 👈 create this view next

# ✅ Router setup
router = DefaultRouter()
router.register(r"courses", CourseViewSet, basename="course")
router.register(r"videos", VideoViewSet, basename="video")

urlpatterns = [
    path("admin/", admin.site.urls),    # Django admin
    path("api/", include(router.urls)), # Rest API endpoints

    # ✅ AUTH APIs for login
    path("api/auth/token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/me/", current_user, name="current-user"),

    # ✅ React will use this to load courses
   
    path("api/auth/", include("accounts.urls")),

]
