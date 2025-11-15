# backend/create_superuser.py
from django.contrib.auth import get_user_model
User = get_user_model()

import os
USERNAME = os.getenv("ADMIN_USERNAME", "admin")
EMAIL = os.getenv("ADMIN_EMAIL", "admin@example.com")
PASSWORD = os.getenv("ADMIN_PASSWORD", "Admin@12345")

if not User.objects.filter(username=USERNAME).exists():
    User.objects.create_superuser(username=USERNAME, email=EMAIL, password=PASSWORD)
    print("Superuser created:", USERNAME)
else:
    print("Superuser already exists:", USERNAME)
