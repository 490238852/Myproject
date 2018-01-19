
from django.conf.urls import url,include
from django.contrib import admin



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^APP/', include('APP.app_url')),
    url(r'^API/', include('API.api_urls')),
    url(r'^CRM/', include('CRM.crm_urls')),
]
