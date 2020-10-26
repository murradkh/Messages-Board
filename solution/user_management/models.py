from django.db import models
from django.contrib.auth.models import User
from django.apps import apps
from currency_management.models import Currency


class Profile(models.Model):
    usr = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    favorite_currency = models.ForeignKey(Currency, related_name="profiles", on_delete=models.SET_NULL, null=True)
    img = models.FilePathField(path="user_management/static/images")
