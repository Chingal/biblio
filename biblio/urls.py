from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers
from biblio.apis.viewsets import PerfilViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'perfil', PerfilViewSet )
router.register(r'accounts', UserViewSet )

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'biblio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(router.urls) ),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework' )),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('biblio.apps.inicio.urls')),
    url(r'^libro/', include('biblio.apps.libros.urls')),
    url(r'^autor/', include('biblio.apps.autores.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)