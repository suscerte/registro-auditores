from django.conf.urls import patterns, include, url
from django.contrib.auth.views import logout

from django.contrib import admin
from personas.views import PersonalesView
from curriculum.views import PerfilView, EducacionView, LaboralView, CompetenciaView, HabilidadView, ConocimientoView, IdiomaView
from auth.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'auditores_suscerte.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^curriculum/', include('curriculum.urls')),
    url(r'logout/',logout,{'next_page':'/'}, name='salir'),
    url(r'login/', Auth.as_view(), name='auth'),
    url(r'cambiar_clave/', cambiar_clave, name='cambiar_clave'),
    url(r'^perfil/personales$', PersonalesView.as_view(), name='personales'),
    url(r'^perfil/educacion/(?P<palabra>\w+)/(?P<educacion_id>[\d]+)*$', EducacionView.as_view(), name='educacion'),
    url(r'^perfil/laboral/(?P<palabra>\w+)/(?P<laboral_id>[\d]+)*$', LaboralView.as_view(), name='laboral'),
    url(r'^perfil/conocimiento/(?P<palabra>\w+)/(?P<conocimiento_id>[\d]+)*$', ConocimientoView.as_view(), name='conocimiento'),
    url(r'^perfil/competencia/(?P<palabra>\w+)/(?P<competencia_id>[\d]+)*$', CompetenciaView.as_view(), name='competencia'),
    url(r'^perfil/habilidad/(?P<palabra>\w+)/(?P<habilidad_id>[\d]+)*$', HabilidadView.as_view(), name='habilidad'),
    url(r'^perfil/idioma/(?P<palabra>\w+)/(?P<idioma_id>[\d]+)*$', IdiomaView.as_view(), name='idioma'),
    url(r'^perfil/$', PerfilView.as_view(), name='perfil'),
    url(r'^$', Auth.as_view(), name='inicio'),
)
