from django.conf.urls import patterns, url
from views import CreateAutor, ListAutor

urlpatterns = patterns('biblio.apps.autores.views',
    url(r'^add/$',CreateAutor.as_view() ,name="add"),
    url(r'^list/$',ListAutor.as_view() ,name="list"),
)