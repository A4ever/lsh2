from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  # اضافه شده
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap
from shop.sitemaps import ProductSitema
# core/urls.py
from django.http import JsonResponse

def health_check(request):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path('health/', health_check),  # اضافه کردن این خط
    # ... بقیه مسیرها


sitemaps = {"static": StaticViewSitemap, "products": ProductSitemap}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("", include("website.urls")),
    path("accounts/", include("accounts.urls")),
    path("shop/", include("shop.urls")),
    path("cart/", include("cart.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("order/", include("order.urls")),
    path("payment/", include("payment.urls")),
    path("review/", include("review.urls")),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]

handler404 = "core.error_views.error_404"

# همیشه استاتیک‌ها را اضافه کنید (برای کار با collectstatic)
urlpatterns += staticfiles_urlpatterns()

# فقط در حالت توسعه فایل‌های مدیا را سرویس دهید
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)