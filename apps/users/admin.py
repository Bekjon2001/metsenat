from django.contrib import admin

from apps.users.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    ordering = ('phone_number',)
