import os
import django

# Tell Django where settings.py is
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# Load Django
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

ADMIN_EMAIL = "admin@example.com"
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

# Create superuser only if not exists
if not User.objects.filter(username=ADMIN_USERNAME).exists():
    User.objects.create_superuser(
        username=ADMIN_USERNAME,
        email=ADMIN_EMAIL,
        password=ADMIN_PASSWORD
    )
    print("Superuser created!")
else:
    print("Superuser already exists, skipping.")
