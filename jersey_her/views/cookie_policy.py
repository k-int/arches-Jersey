# Imports
import uuid

# Django
from django.views.generic import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.utils.translation import gettext as _

from arches.app.views.base import BaseManagerView


class CookiePolicy(BaseManagerView):

    def get(self, request):
        context = self.get_context_data(main_script="views/cookie_policy")
        context["nav"]["title"] = _("Jersey Heritage HER Cookie Policy")
        return render(request, "views/cookie_policy.htm", context)
