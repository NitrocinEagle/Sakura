# -*- coding: utf8 -*-
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.views.generic import FormView, TemplateView
from django.views.generic.base import View
from django.contrib.auth.forms import AuthenticationForm


class BonusesView(TemplateView):
    template_name = 'index/index.html'

