from django.contrib import admin

from .models import Setup

@admin.action(description='Mark selected as in UEFI mode')
def uefi_on(modeladmin, request, queryset):
    queryset.update(uefi=True)
    
@admin.action(description='Mark selected as not in UEFI mode')
def uefi_off(modeladmin, request, queryset):
    queryset.update(uefi=False)
    
class SetupAdmin(admin.ModelAdmin):
    list_display = ['name', 'ip']
    search_fields = ['name', 'ip']
    actions = [uefi_on, uefi_off]
    
admin.site.register(Setup, SetupAdmin)
