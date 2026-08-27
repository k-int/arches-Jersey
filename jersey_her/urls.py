from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path, re_path

from arches.app.views.main import index
from jersey_her.views.index_je import index_je
from jersey_her.views.cookie_policy import CookiePolicy

urlpatterns = [
    re_path(r"^en$", index, name="home_english"),
    re_path(r"^je$", index_je, name="home_jerrais"),
    re_path(r"^cookie_policy", CookiePolicy.as_view(), name="cookie_policy"),
    path("", include("arches_pdf_exporting.urls")),
]

# Ensure Arches core urls are superseded by project-level urls
urlpatterns.append(path("", include("arches.urls")))

# Adds URL pattern to serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Only handle i18n routing in active project. This will still handle the routes provided by Arches core and Arches applications,
# but handling i18n routes in multiple places causes application errors.
if settings.ROOT_URLCONF == __name__:
    if settings.SHOW_LANGUAGE_SWITCH is True:
        urlpatterns = i18n_patterns(*urlpatterns)

    urlpatterns.append(path("i18n/", include("django.conf.urls.i18n")))
