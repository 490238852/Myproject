from django.conf.urls import url,include
from rest_framework import routers
from CRM import rest_views


router = routers.DefaultRouter()
router.register(r'users',rest_views.AccountViewset)
router.register(r'role',rest_views.RoleViewset)
router.register(r'customer',rest_views.CustomerViewset)
router.register(r'menu',rest_views.MenuViewset)
router.register(r'source',rest_views.SourceViewset)

urlpatterns = [
    url(r'^',include(router.urls)),
]


