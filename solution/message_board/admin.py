from django.contrib import admin
from .models import Message


class UserAdmin(admin.ModelAdmin):
    pass


class MessageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Message, MessageAdmin)

