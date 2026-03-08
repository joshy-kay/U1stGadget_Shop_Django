"""Reset or create a demo admin user for the presentation.

Usage:
  python scripts/reset_admin.py

This will set the `admin` user's password to `admin123` and ensure
the account has `is_staff` and `is_superuser` set. Change the password
after the presentation for security.
"""
import os
import sys
from pathlib import Path

# Ensure project root is on sys.path so Django settings can be imported
sys.path.append(str(Path(__file__).resolve().parent.parent))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'u1stgadget.settings')

import django
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = 'admin'
password = 'admin123'
email = 'admin@example.com'

user = User.objects.filter(username=username).first()
if user:
    user.set_password(password)
    user.is_staff = True
    user.is_superuser = True
    user.save()
    print('Updated existing admin user: password set to admin123, staff/superuser True')
else:
    User.objects.create_superuser(username, email, password)
    print('Created admin superuser with password admin123')
