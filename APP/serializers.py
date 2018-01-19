from rest_framework import serializers
from APP.models import *



class UserInfoSerializers(serializers.Serializer):
    nid = serializers.CharField(read_only=True)
    username = serializers.CharField(max_length=32,error_messages={'null':'不能为空'})
    password = serializers.CharField(max_length=64)
    age = serializers.IntegerField()
    def create(self, validated_data):
        return UserInfo.objects.create(**validated_data)
    def update(self, instance, validated_data):
        # instance.nid = validated_data.get('nid',instance.nid)
        instance.username = validated_data.get('username',instance.username)
        instance.password = validated_data.get('password',instance.password)
        instance.age = validated_data.get('age',instance.age)
        instance.save()
        return instance