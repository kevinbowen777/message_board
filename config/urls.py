from django.conf import settings  # noqa:F401
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("posts.urls")),
]

"""
if settings.DEBUG:
    import debug_toolbar  # noqa: F401

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
"""
