from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    passcode = models.IntegerField(validators=[MaxValueValidator(9999), MinValueValidator(1000)]
                                   , null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
