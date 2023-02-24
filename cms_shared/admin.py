from cms_tenant.models import PolicyType
from django.contrib import admin

@admin.register(PolicyType)
class PolicyTypeAdmin(admin.ModelAdmin):
        list_display = ('id', 'name',)
