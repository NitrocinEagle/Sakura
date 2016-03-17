# -*- coding: utf-8 -*-
from django.conf.urls import url, include

urlpatterns = [
    url(r'^menu/', include('app.adm.menu.urls', namespace="menu")),
]