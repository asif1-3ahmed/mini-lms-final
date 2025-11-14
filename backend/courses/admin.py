from django.contrib import admin
from .models import Course, Video

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created_by", "created_at")
    search_fields = ("title", "description")

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "created_at")
    search_fields = ("title", "course__title")
