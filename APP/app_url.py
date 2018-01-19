from django.conf.urls import url,include
from django.contrib import admin
from APP import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^user/$',views.users),
    url(r'^user/(?P<pk>[0-9]+)/$',views.users_detail),
    url(r'^user/(?P<name>\w*)/(?P<uid>\d*)', views.user_index),
    url(r'^userclass',views.UserRequest.as_view()),
    url(r'^UserLogin/$', views.UserLogin,name='UserLogin'),
    url(r'^UserLogout/$', views.UserLogout,name='UserLogout'),
    url(r'^UserResgister/$',views.UserResgister,name='UserResgister'),
]