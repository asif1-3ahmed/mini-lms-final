from django.db import models
from django.conf import settings
from courses.models import Course


class Quiz(models.Model):
    course = models.ForeignKey(Course, related_name="quizzes", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name="questions", on_delete=models.CASCADE)
    text = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255, blank=True)
    option_d = models.CharField(max_length=255, blank=True)
    correct_option = models.CharField(max_length=1)

    def __str__(self):
        return self.text
