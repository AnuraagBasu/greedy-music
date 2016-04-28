__author__ = 'anuraagbasu'

from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^music/', include('music.urls', namespace="music")),
]

if not settings.DEBUG:
    urlpatterns += patterns('',(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),)