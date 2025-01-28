from django.contrib import admin
from .models import StudentSponsor

# StudentSponsor modelini admin panelida ko‘rsatish
class StudentSponsorAdmin(admin.ModelAdmin):
    list_display = ('student', 'sponsor', 'amount', 'is_verified', 'payment_method', 'created_at', 'updated_at')
    search_fields = ('student__phone_number', 'sponsor__phone_number', 'amount')
    list_filter = ('is_verified', 'payment_method')
    ordering = ('-created_at',)

    fieldsets = (
        (None, {
            'fields': ('student', 'sponsor', 'amount', 'is_verified', 'payment_method')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

admin.site.register(StudentSponsor, StudentSponsorAdmin)

