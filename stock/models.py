from django.db import models

import random

class Stock(models.Model):
    name = models.CharField(max_length=40)
    ticker = models.CharField(max_length=4, default="NULL")
    description = models.TextField(null=True, blank=True)
    currency = models.ForeignKey('Currency', null=True, on_delete=models.SET_NULL)
    logo = models.ImageField(null=True, blank=True)

    def get_random_price(self):
        return random.randint(0, 3000)

    def __str__(self):
        return f"{self.ticker}"

class Currency(models.Model):
    name = models.CharField(max_length=40)
    ticker = models.CharField(max_length=4)
    sign = models.CharField(max_length=1)

    def __str__(self):
        return self.sign
