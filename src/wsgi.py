import os
from django.core.wsgi import get_wsgi_application

from src.settings.base import DEBUG

if DEBUG : 
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings.local")
else :
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings.production")

application = get_wsgi_application()
