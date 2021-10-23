# Bismillah Hir Rehman Nir Rahim

"""
WSGI config for facebookgame project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""
from waitress import serve

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'facebookgamer.settings')

application = get_wsgi_application()
