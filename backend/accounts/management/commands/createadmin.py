from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = "Creates a default admin user if not exists"

    def handle(self, *args, **options):
        User = get_user_model()
        username = os.getenv("DJANGO_ADMIN_USERNAME", "admin")
        password = os.getenv("DJANGO_ADMIN_PASSWORD", "admin123")
        email = os.getenv("DJANGO_ADMIN_EMAIL", "admin@example.com")

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                password=password,
                email=email
            )
            self.stdout.write(self.style.SUCCESS(f"Admin '{username}' created."))
        else:
            self.stdout.write(self.style.WARNING(f"Admin '{username}' already exists."))
