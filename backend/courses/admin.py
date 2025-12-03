from django.contrib import admin
from .models import Course, Video

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "duration", "category", "created_by", "created_at")
    search_fields = ("title", "description", "category")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("category", "duration", "created_by")
    ordering = ("-created_at",)
    readonly_fields = ("created_by", "created_at")

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "created_at")
    search_fields = ("title", "course__title")
