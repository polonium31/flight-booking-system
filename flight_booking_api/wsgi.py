"""
WSGI config for flight_booking_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

if os.environ['ENV'] in ['PRODUCTION']:
    setting = 'flight_booking_api.settings.production'
else:
    setting = 'flight_booking_api.settings.development'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', setting)

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
