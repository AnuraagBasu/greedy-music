__author__ = 'anuraagbasu'

from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from music import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^tracks', views.showAllTracks, name='showAllTracks'),
    url(r'^track/add', views.addTrack, name='addTrack'),
    url(r'^track/(?P<trackId>[0-9]+)/$', views.trackDetail, name='trackDetail'),
    url(r'^track/(?P<trackId>[0-9]+)/edit/$', views.trackUpdate, name='trackUpdate'),

    url(r'^genres', views.showAllGenres, name='showAllGenres'),
    url(r'^genre/add', views.addGenre, name='addGenre'),
    url(r'^genre/(?P<genreId>[0-9]+)/$', views.genreDetail, name='genreDetail'),
    url(r'^genre/(?P<genreId>[0-9]+)/edit/$', views.genreUpdate, name='genreUpdate'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)