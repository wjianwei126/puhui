from django.conf.urls import include, url
from django.contrib import admin
from api import urls
from web import weburls
urlpatterns = [
    # Examples:
    # url(r'^$', 'puhui.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(urls)),
    url(r'^puhui/', include(weburls)),
    url(r'^zrq/', include(weburls)),
]
