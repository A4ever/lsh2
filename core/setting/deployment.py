from .base import *
import os

DEBUG = False
SITE_ID = 1

ALLOWED_HOSTS = [
    'localhost',
    '0.0.0.0',
    '.liara.run',
    '.yourdomain.com',
    os.getenv('LIARA_APP_NAME', '') + '.liara.run'
]

# تنظیمات امنیتی
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# فایل‌های استاتیک
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = []

# غیرفعال کردن ابزارهای توسعه
INSTALLED_APPS = [app for app in INSTALLED_APPS if app not in ["debug_toolbar", "drf_yasg"]]
MIDDLEWARE = [m for m in MIDDLEWARE if m != "debug_toolbar.middleware.DebugToolbarMiddleware"]