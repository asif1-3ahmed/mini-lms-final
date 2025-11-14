#!/usr/bin/env python
import os
import sys
import django

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
    django.setup()
    
    from django.core.management import call_command
    
    print("=" * 60)
    print("Starting Django application with automatic migrations...")
    print("=" * 60)
    
    # Run migrations
    try:
        print("\n[1/2] Running database migrations...")
        call_command("migrate", "--noinput", verbosity=2)
        print("✓ Migrations completed successfully!")
    except Exception as e:
        print(f"✗ Migration error: {e}")
        sys.exit(1)
    
    # Start gunicorn
    print("\n[2/2] Starting gunicorn server...")
    print("=" * 60)
    os.execvp("gunicorn", ["gunicorn", "core.wsgi", "--log-file", "-", "--bind", "0.0.0.0:8000", "--workers", "3"])
