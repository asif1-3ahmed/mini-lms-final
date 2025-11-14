from django.db import models
from apps.courses.models import Course

class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="videos")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    # cloudinary will provide url in uploaded file field
    video = models.FileField(upload_to="videos/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
