from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path, re_path

from arches.app.views.main import index
from .views.index_je import index_je
from .views.resource_count import resource_count
from .views.cookie_policy import CookiePolicy
from .views.html_export_find import html_export_find

urlpatterns = [
    re_path(r"^", include("arches.urls")),
    re_path(r"^en$", index, name="home_english"),
    re_path(r"^je$", index_je, name="home_jerrais"),
    path("resource_count/", resource_count),
    re_path(r"^cookie_policy", CookiePolicy.as_view(), name="cookie_policy"),
    re_path(r"^html_export_find$", html_export_find, name="html_export_find"),
]

# Adds URL pattern to serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Only handle i18n routing in active project. This will still handle the routes provided by Arches core and Arches applications,
# but handling i18n routes in multiple places causes application errors.
if settings.ROOT_URLCONF == __name__:
    if settings.SHOW_LANGUAGE_SWITCH is True:
        urlpatterns = i18n_patterns(*urlpatterns)

    urlpatterns.append(path("i18n/", include("django.conf.urls.i18n")))
