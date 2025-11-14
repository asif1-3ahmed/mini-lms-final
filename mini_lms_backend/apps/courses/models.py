from django.db import models
from apps.users.models import User

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="created_courses")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
