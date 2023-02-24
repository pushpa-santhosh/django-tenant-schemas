from django.contrib import admin
from cms_tenant.models import Policy


@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
        list_display = ('id', 'name')
