from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("export_page", include("djangocms_export_page.urls")),
]
urlpatterns += i18n_patterns(
    re_path(r"^", include("cms.urls")),
)
