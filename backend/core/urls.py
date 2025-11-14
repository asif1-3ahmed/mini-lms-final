from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def health_check(request):
    """Health check endpoint — no auth required"""
    return JsonResponse({"status": "ok", "message": "Backend is running"})

urlpatterns = [
    path("health/", health_check, name="health"),
    path("admin/", admin.site.urls),
    path("api/auth/", include("accounts.urls")),
    path("api/", include("courses.urls")),
    path("api/", include("quizzes.urls")),
]
