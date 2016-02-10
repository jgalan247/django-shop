# -*- coding: utf-8
from __future__ import unicode_literals

from django.test import TestCase
from shop.money import Money
from .models import Commodity


class MoneyFieldTest(TestCase):
    def setUp(self):
        super(MoneyFieldTest, self).setUp()
        Commodity.objects.create(price=Money(1), product_name="One Euro")

    def test_money_field_equal(self):
        Commodity.objects.create().save()
        commodity = Commodity.objects.first()
        self.assertEqula(commodity.pk, 1)
