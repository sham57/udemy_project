from django.contrib import admin

from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'hire_date','is_mvp')
    list_display_links=('name', 'hire_date')
    list_editable=("is_mvp",)
    search_fields=('name', 'is_mvp','email')
    list_per_page=5


admin.site.register(Realtor, RealtorAdmin)

