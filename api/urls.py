from django.conf.urls import patterns, url
from api import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^personajes/offset/(?P<offset_id>\d+)/$', views.personajes, name='personajes_paginado'),
    url(r'^personajes/$', views.personajes, name='personajes_default'),
    url(r'^personajes/id/(?P<personaje_id>\d+)/$', views.personajeID, name='personajes_ID'),
    url(r'^comics/offset/(?P<offset_id>\d+)/$', views.comics, name='comic_paginado'),
    url(r'^comics/$', views.comics, name='comic_default'),
    url(r'^comics/id/(?P<comic_id>\d+)/$', views.comicID, name='comic_ID'),
    url(r'^creadores/offset/(?P<offset_id>\d+)/$', views.creadores, name='creadores_paginado'),
    url(r'^creadores/$', views.creadores, name='creadores_default'),
    url(r'^creadores/id/(?P<creador_id>\d+)/$', views.creadorID, name='Creadores_ID')

)