# -*- coding: utf8 -*-
from django.http import HttpResponseRedirect
from django.views.generic import FormView


class CallBackView(FormView):
    template_name = 'index/index.html'
