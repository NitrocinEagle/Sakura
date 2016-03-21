# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Order(models.Model):
    comments = models.TextField(blank=True,
                                verbose_name=u"Комментарии к заказу")

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __unicode__(self):
        return u'Заказ %s' % self.id
