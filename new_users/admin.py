# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import Group, User

from new_users.models import CmsUser, CmsGroup

# Register your models here.
class GroupAdmin(BaseGroupAdmin):
    pass
class UserAdmin(BaseUserAdmin):
    #多显示一个date_joined字段
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff','date_joined')


# admin.site.unregister(User)
admin.site.register(CmsUser, UserAdmin)
admin.site.register(CmsGroup, GroupAdmin)

#隐藏Authentication and Authorizatio下的group菜单
admin.site.unregister(Group)
