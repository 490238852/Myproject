from django.contrib import admin
from APP import models

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('nid', 'username','password', 'age')#页面上展示的字段
    list_filter = ('username', 'age')#右侧的导航栏
    search_fields = ('username', 'age')#搜索框内的条件

admin.site.register(models.UserInfo,UserInfoAdmin)

# Register your models here.
