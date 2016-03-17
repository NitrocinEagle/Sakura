# -*- coding: utf8 -*-
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

class RollsView(TemplateView):
    template_name = 'index/index.html'

