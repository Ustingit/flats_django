from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^apartments/', include('apartments.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]