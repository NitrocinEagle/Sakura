# -*- coding: utf-8 -*-
from django.conf.urls import url, include

urlpatterns = [
    url(r'^menu/', include('app.adm.menu.urls', namespace="menu")),
    url(r'^order/', include('app.adm.order.urls', namespace="order")),
]