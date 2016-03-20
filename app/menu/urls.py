# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^rolls/', TemplateView(template_name="site/index/index.html"), name="rolls"),
    url(r'^sushi/', TemplateView(template_name="site/index/index.html"), name="sushi"),
    url(r'^tempura/', TemplateView(template_name="site/index/index.html"), name="tempura"),
    url(r'^sets/', TemplateView(template_name="site/index/index.html"), name="sets"),
]
