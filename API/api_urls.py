from django.conf.urls import url,include
from API import views
from rest_framework import routers, serializers, viewsets
from API.rest_views import UserViewSet




router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
# router.register(r'')



urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^snippet_list/$', views.snippet_list),
    url(r'^snippet_detail/(?P<pk>[0-9]+)/$', views.snippet_detail),
]