from django.conf.urls import url, include
from .views import register
from django.views.generic.base import RedirectView

urlpatterns = [
    url("", include("django.contrib.auth.urls")),
    url("register/", register, name="register"),
    url("", RedirectView.as_view(url='login/')),

]
