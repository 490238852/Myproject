from rest_framework import serializers
from CRM import models

class AccountSerialisers(serializers.ModelSerializer):    #HyperlinkedModelSerializer展示超链接
    class Meta:
        depth = 1    #序列化展示的深度(和ModelSerializer配合使用)
        model = models.Account
        fields = ('url','name','email','is_active','is_admin','role','customer')   #url是修改自己

class RoleSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Role
        fields = ('url','name','menus')

class CustomerSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Customer
        fields = ('name','qq','weixin','phone','email','source','referral_from','consult_courses','content','status','tags','consultant','date',)


class MenuSeriailzers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Menu
        fields = ('name','url_type','url','order')

class SourceSeriailzers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Source
        fields = ('name',)