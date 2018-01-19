from django.contrib import admin

# Register your models here.
from CRM import models

class AccountAdmin(admin.ModelAdmin):
    list_display=('name','email','role','customer','is_active','is_admin')
    list_filter=('name','email','role')
    search_fields=('name','email','is_active','is_admin')


class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


admin.site.register(models.Account,AccountAdmin)
admin.site.register(models.Role,RoleAdmin)
admin.site.register(models.Menu)
admin.site.register(models.SubMenu)

