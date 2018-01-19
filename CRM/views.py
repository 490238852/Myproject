from django.shortcuts import render
from CRM import models


def ClassStudents(request):
    obj = models.ClassList.objects.all()
    obj_list = models.ClassList.objects.values('semester','course__classlist')   #正想查询，双下划线
    for raw in obj:
        raw.courserecord_set.all()   #foreighKey字段反向查询CourseRecord表中的所有数据（点+表名小写+下划线+set）


def Account(request):
    account_obj = models.Account.objects.all()
    account_obj_role = models.Account.objects.values('name','role','role__name','')
    role_obj = models.Role.objects.filter(id=1).first()
    role_obj.menus.add(1)
    role_obj.menus.add(1,2,3,4)
    role_obj.menus.add(*[1,2,3,])
    role_obj.menus.remove(*[1,2,3,])
    role_obj.menus.clear()
    role_obj.menus.set(*[3])   #先clear在add
    role_obj.menus.all()      #manytomany直接取关联表的数据
    role_obj.menus.filter(id__gt=2)   #二次查询