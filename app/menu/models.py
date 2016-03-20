# -*- coding: utf8 -*-
from django.db import models

CATEGORY_LIST = (
    ("sushi", u"Суши"),
    ("rolls", u"Роллы"),
    ("sets", u"Наборы"),
    ("soups", u"Супы"),
    ("souces", u"Соусы"),
    ("desserts", u"Десерты"),
    ("tempura", u"Темпура"),
)

TAG_LIST = (
    ("new", u"Новинка"),
    ("spicy", u"Острый"),
    ("veg", u"Вегетерианский"),
    ("hit", u"Хит"),
)


# Тестовый пользователь: test 1234test
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"Название товара")
    category = models.CharField(choices=CATEGORY_LIST, max_length=20)
    image = models.ImageField(upload_to="products/", blank=True,
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
