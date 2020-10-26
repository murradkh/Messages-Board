from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('message-board/', include("message_board.urls")),
    path(r"user-management/", include("user_management.urls")),
    path(r"", RedirectView.as_view(url='message-board/')),

]
