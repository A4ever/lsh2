import os
from decouple import config
from django.core.asgi import get_asgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    config("SETTING_PATH", default="core.settings.deployment"),
)

application = get_asgi_application()