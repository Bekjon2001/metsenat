from django.contrib import admin

from .models import University, PaymentMethod

class UniversityAdmin(admin.ModelAdmin):
    list_display = ('guid','name', 'contract_amount', 'created_at',)
    search_fields = ('name',)
    list_filter = ('created_at',)
    ordering = ('created_at',)

admin.site.register(University, UniversityAdmin)

class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('id','name',)

admin.site.register(PaymentMethod, PaymentMethodAdmin)