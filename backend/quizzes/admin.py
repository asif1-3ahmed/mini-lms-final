from django.contrib import admin
from .models import Quiz, Question

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("title", "course")
    search_fields = ("title", "course__title")

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "quiz", "correct_option")
    search_fields = ("text", "quiz__title")
