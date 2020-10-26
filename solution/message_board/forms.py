from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


class CreateMessageForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Title"
        })
    )
    message = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Message content!"
        })

    )


class UpdateMessageForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Title"
        })
    )
    message = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Message content!"
        })

    )
    passcode = forms.IntegerField(max_value=9999, min_value=1000,
                                  widget=forms.NumberInput(attrs={'placeholder': 'Your Passcode'}), required=False)


class DeleteMessageForm(forms.Form):
    passcode = forms.IntegerField(max_value=9999, min_value=1000,
                                  widget=forms.NumberInput(attrs={'placeholder': 'Your Passcode'}))


class SearchForm(forms.Form):
    search_title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Type Title Name"
        })
    )
