"""
ARCHES - a program developed to inventory and manage immovable cultural heritage.
Copyright (C) 2013 J. Paul Getty Trust and World Monuments Fund

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

import re
import urllib.request, urllib.error, urllib.parse
from urllib.parse import urlparse
from arches import __version__
from arches.app.models.system_settings import settings
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, HttpResponse, HttpResponseRedirect
from django.utils import translation


def index_je(request):
    return render(
        request,
        "index_je.htm",
        {
            "main_script": "index",
            "active_page": "Home",
            "app_title": settings.APP_TITLE,
            "copyright_text": "Touos les drouaits rêsèrvés",
            "copyright_year": settings.COPYRIGHT_YEAR,
            "app_version": settings.APP_VERSION,
            "version": __version__,
            "show_language_swtich": settings.SHOW_LANGUAGE_SWITCH,
        },
    )
