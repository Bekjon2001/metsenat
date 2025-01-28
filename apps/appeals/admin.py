from django.contrib import admin

from .models import Appeal

class AppealAdmin(admin.ModelAdmin):
    list_display = ('sponsor',)
    list_filter = ('created_at',)
    ordering = ('created_at',)

admin.site.register(Appeal, AppealAdmin)



