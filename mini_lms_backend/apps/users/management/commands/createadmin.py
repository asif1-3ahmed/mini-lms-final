from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

User = get_user_model()

class Command(BaseCommand):
    help = "Create initial admin superuser from env vars"

    def handle(self, *args, **options):
        username = os.getenv("ADMIN_USERNAME", "Asif")
        email = os.getenv("ADMIN_EMAIL", "admin@example.com")
        password = os.getenv("ADMIN_PASSWORD", "Qwer1234@123")
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password, role="ADMIN")
            self.stdout.write(self.style.SUCCESS("Admin user created"))
        else:
            self.stdout.write("Admin user already exists")
