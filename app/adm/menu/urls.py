# -*- coding: utf-8 -*-
from django.conf.urls import url
from views import AddProductView, ListProductsView

urlpatterns = [
    url(r'^add/$', AddProductView.as_view(), name="new_product"),
    url(r'^products/$', ListProductsView.as_view(), name="view_product"),
]
