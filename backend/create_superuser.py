import os
from django.contrib.auth import get_user_model

User = get_user_model()

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123")
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "admin@example.com")

if not User.objects.filter(username=ADMIN_USERNAME).exists():
    print("🚀 Creating default superuser...")
    User.objects.create_superuser(
        username=ADMIN_USERNAME,
        email=ADMIN_EMAIL,
        password=ADMIN_PASSWORD
    )
else:
    print("✔ Superuser already exists. Skipping...")
