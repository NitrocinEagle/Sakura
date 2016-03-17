# -*- coding: utf8 -*-
from django.views.generic import TemplateView


class UserView(TemplateView):
    template_name = 'site/index/user.html'
