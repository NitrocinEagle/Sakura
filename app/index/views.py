# -*- coding: utf8 -*-
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.views.generic import FormView
from django.views.generic.base import View, TemplateView
from django.contrib.auth.forms import AuthenticationForm


class LoginFormView(FormView):
    form_class = AuthenticationForm

    template_name = "site/index/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/login")


class IndexView(TemplateView):
    template_name = 'site/index/index.html'
