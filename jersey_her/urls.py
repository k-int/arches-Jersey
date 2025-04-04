from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

from django.contrib import admin
from django.urls import path, include

from .views.resource_count import resource_count
from .views.cookie_policy import CookiePolicy

urlpatterns = [
    url(r'^', include('arches.urls')),
    path('resource_count/', resource_count),
    url(r"^cookie_policy", CookiePolicy.as_view(), name="cookie_policy")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.SHOW_LANGUAGE_SWITCH is True:
    urlpatterns = i18n_patterns(*urlpatterns)
