from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    path ("",views.index),
    path ("studioSongs",views.studioSongs),
    path ("studioDeleteSongs",views.studioDeleteSongs),
    path ("studioDeleteAlbums",views.studioDeleteAlbums),
    path ("studio",views.studio),
    path ("studioAlbums",views.studioAlbums),
]

urlpatterns += staticfiles_urlpatterns()