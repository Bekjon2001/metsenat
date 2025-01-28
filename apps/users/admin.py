from django.contrib import admin
from apps.users.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    """
    Admin panelida CustomUser modelini sozlash.
    """
    list_display = ('id','first_name', 'email', 'phone_number', 'user_type', 'date_joined', 'is_active',)

    search_fields = ('first_name', 'phone_number')

    list_filter = ('user_type', 'is_active')

    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'phone_number')
        }),
        ('Permissions', {
            'fields': ('user_type', 'is_active')
        }),
        ('Important dates', {
            'fields': ('date_joined',)
        }),
    )

    list_per_page = 25
    ordering = ('id',)
admin.site.register(CustomUser, CustomUserAdmin)
