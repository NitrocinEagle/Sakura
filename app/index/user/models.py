# django -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.utils.timezone import now

STATUS_CHOICES = (
    (u"Новичок", u"Новичок"),
    (u"Любитель", u"Любитель"),
    (u"Гурман", u"Гурман"),
    (u"Сушимен", u"Сушимен")
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="User")
    full_name = models.CharField(max_length=128, verbose_name=u"ФИО")
    avatar = models.ImageField(upload_to="avatars", blank=True)
    total_order_sum = models.FloatField(verbose_name=u"Итого заказано на сумму",
                                        default=0.0)
    total_order_count = models.IntegerField(verbose_name=u"Итого заказов",
                                            default=0)
    phone_number = models.CharField(blank=True, max_length=11,
                                    verbose_name=u"Номер телефона")
    email = models.EmailField(verbose_name=u"Электронный адрес")
    date_joined = models.DateField(verbose_name=u"Дата регистрации",
                                   default=now())
    status = models.CharField(default=u"Новичок", choices=STATUS_CHOICES,
                              verbose_name=u"Статус пользователя",
                              max_length=10)
    about = models.TextField(blank=True, verbose_name=u"О себе")

    def __unicode__(self):
        return u'%s' % self.full_name
