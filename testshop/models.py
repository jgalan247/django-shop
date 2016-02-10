# -*- coding: utf-8
from __future__ import unicode_literals

from django.db import models
from shop.models.defaults.customer import Customer  # nopyflakes
from shop.money.fields import MoneyField
from shop.models.product import BaseProduct, BaseProductManager


class Commodity(BaseProduct):
    product_name = models.CharField(max_length=255)
    price = MoneyField(decimal_places=3, null=True)

    objects = BaseProductManager()

    lookup_fields = ('product_name__icontains',)
