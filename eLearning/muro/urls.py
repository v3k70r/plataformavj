from django.conf.urls import url
from . import views as muro_views

urlpatterns = [
    url(r'^$', muro_views.muro, name='muro'),
    url(r'^leer', muro_views.muroVer, name='muroVer'),
    url(r'^anunciar', muro_views.muroAdmin, name='muroAdmin'),
    url(r'^(?P<slug>[\w-]+)/$', muro_views.anuncio, name='anuncio'),
]
