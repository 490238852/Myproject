from rest_framework import viewsets
from CRM.models import *
from CRM import rest_serializers


class AccountViewset(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = rest_serializers.AccountSerialisers

class RoleViewset(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = rest_serializers.RoleSerializers

class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = rest_serializers.CustomerSerializers

class MenuViewset(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = rest_serializers.MenuSeriailzers


class SourceViewset(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = rest_serializers.SourceSeriailzers