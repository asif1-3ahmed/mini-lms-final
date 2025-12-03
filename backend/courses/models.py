from django.db import models
from django.conf import settings
from django.utils.text import slugify

class Course(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, blank=True)

    # NEW FIELDS FOR CAREER GUIDANCE WEBSITE
    duration = models.CharField(max_length=100, blank=True)
    overview = models.TextField(blank=True)
    skills = models.JSONField(default=list, blank=True)
    modules = models.JSONField(default=list, blank=True)
    career_paths = models.JSONField(default=list, blank=True)
    roadmap = models.JSONField(default=list, blank=True)
    faq = models.JSONField(default=list, blank=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Auto slug generation
    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)
            slug = base
            counter = 1
            while Course.objects.filter(slug=slug).exists():
                slug = f"{base}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Video(models.Model):
    course = models.ForeignKey(Course, related_name="videos", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    storage_url = models.URLField()
    duration = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course.title} - {self.title}"
