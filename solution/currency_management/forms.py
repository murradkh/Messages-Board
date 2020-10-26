from django import forms
from .models import Currency


class CurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = ("currency_name",)
        labels = {
            "currency_name": "Preferred Currency"
        }
