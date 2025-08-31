"""
This file makes the ASGI callable configuration accessible
for the demo_project folder as a module-level variable named "application".
"""

# I used this website for information:
# https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/

import os
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo_project.settings')

application = get_asgi_application()