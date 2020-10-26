from django.apps import apps
from django.db import models


class Currency(models.Model):
    currency_name = models.CharField(max_length=3,
                                     choices=apps.get_app_config('currency_management').CURRENCIES_NAME)
    value = models.FloatField()
