from django.db import models

# Create your models here.


class UserInfo(models.Model):     #python manage.py makemigrations    migrate
    nid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32,error_messages={'null':'不能为空'})
    password = models.CharField(max_length=64)
    age = models.IntegerField()
    class Meta:
        verbose_name="用户表"
        verbose_name_plural="用户"


# class Text(models.Model):
#     nid = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=32,null=True)
#     text = models.ForeignKey(UserInfo,to_field=nid)
#     class Meta:
#         db_table="API_text_1"
#         verbose_name="测试表"