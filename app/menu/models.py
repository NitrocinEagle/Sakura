# -*- coding: utf8 -*-
from django.db import models

CATEGORY_LIST = (
    ("sushi", u"Суши"),
    ("rolls", u"Роллы"),
    ("sets", u"Наборы"),
    ("tempura", u"Темпура"),
)

TAG_LIST = (
    ("New", u"Новинка"),
    ("Spicy", u"Острый"),
    ("Veg", u"Вегетерианский"),
    ("Hit", u"Хит"),
)


# Тестовый пользователь: test 1234test
class Product(models.Model):
    def get_upload_folder(self):
        return "products/" + str(self.category)

    name = models.CharField(max_length=100, verbose_name=u"Название товара")
    category = models.CharField(choices=CATEGORY_LIST, max_length=20)
    image = models.ImageField(upload_to=get_upload_folder(), blank=True,
                              width_field=200, height_field=200,
                              verbose_name=u"изображение товара")
    price = models.FloatField(verbose_name=u"Цена", default=0.0, )
    is_enabled = models.BooleanField(verbose_name=u"В продаже ли товар",
                                     default=True)
    weight = models.IntegerField(verbose_name=u"Вес в грамах", default=0)
    calorie = models.IntegerField(verbose_name=u"Килокаллории", default=0)
    tag = models.CharField(verbose_name=u"Бирка", max_length=10,
                           choices=TAG_LIST, blank=True, default=None)
    about = models.TextField(blank=True, verbose_name=u"О товаре")

    def __unicode__(self):
        return u'%s' % self.name
