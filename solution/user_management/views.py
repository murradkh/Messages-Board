from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import UserForm
from .models import Profile
# from currency_management.forms import CurrencyForm
# from currency_management.models import Currency


def register(request):
    if request.method == "GET":
        return render(
            request, "registration/register.html",
            {"user_form": UserForm}
        )
    elif request.method == "POST":
        # currency_form = CurrencyForm(request.POST)
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.password = make_password(user.password)
            user.save()
            # currency = Currency.objects.get(currency_name=currency_form.cleaned_data.get("currency_name"))
            Profile(usr=user).save()
            return render(request, "registration/success_registration.html")
        else:
            return render(request, "registration/register.html",
                          {"user_form": user_form,
                           "errors": {**user_form.errors}})

    return redirect(reverse("home"))
