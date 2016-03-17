# -*- coding: utf-8 -*-
from django.conf.urls import url
from rolls.views import RollsView

urlpatterns = [
    url(r'^rolls/', RollsView.as_view(), name="rolls"),
    url(r'^sushi/', RollsView.as_view(), name="sushi"),
    url(r'^tempura/', RollsView.as_view(), name="tempura"),
    url(r'^sets/', RollsView.as_view(), name="sets"),
]
