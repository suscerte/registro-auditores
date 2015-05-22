#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib.auth.views import logout as deslogeo
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import (password_reset,
        password_reset_done, password_reset_confirm,
        password_reset_complete, password_change,
        password_change_done)
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView
from personas.views import PersonalesView
from curriculum.views import (EducacionView, LaboralView, CompetenciaView,
    HabilidadView, ConocimientoView, IdiomaView,
    CitasView, CertificacionView, CursoView,
    VerAuditores, EvaluacionView, revisar_acreditaciones,
    AcreditarView, FijarCitaView, DatosView)
from authentication.views import *
from authentication.forms import (ValidatingSetPasswordForm,
    ValidatingPasswordChangeForm)
from django.contrib.auth.decorators import login_required
import os


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^clave/reestablecer/?$',
        password_reset,
        {'post_reset_redirect': reverse_lazy('password_reset_done'),
         'template_name': 'auth/password_reset_form.html',
         'email_template_name': 'auth/reset_subject.html'},
        name='password_reset'),

    url(r'^clave/solicitud_envio/?$',
        password_reset_done,
        {'template_name': 'auth/password_reset_done.html'},
        name='password_reset_done'),

    url(r'^clave_cambiada/$',
        password_change_done,
        {'template_name': 'auth/clave_cambiada.html'},
        name='password_change_done'),

    url(r'^clave/confirmacion/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
        password_reset_confirm,
        {'post_reset_redirect': reverse_lazy('password_reset_complete'),
         'template_name': 'auth/confirmar_cambiar_clave.html',
         'set_password_form': ValidatingSetPasswordForm},
        name='password_reset_confirm'),

    url(r'^clave/reestablcimiento/completo/$',
        password_reset_complete,
        {'template_name': 'auth/clave_cambiada.html'},
        name='password_reset_complete'),

    url(r'^admin/',
        include(admin.site.urls)),

    url(r'^curriculum/',
        include('curriculum.urls')),

    url(r'logout/',
        deslogeo,
        {'next_page': '/'},
        name='salir'),

    url(r'login/',
        auth,
        name='login'),

    url(r'cambiar_clave/',
        login_required(password_change),
        {'password_change_form': ValidatingPasswordChangeForm,
        'template_name': 'auth/password_reset_form.html',
        'post_change_redirect': 'logout/',
        'extra_context':
            {'cambiar_clave': True,
             'formulario': True,
             'titulo': u'cambiar contraseña',
             'palabra_clave': 'cambiar'},
        },
        name='cambiar_clave'),

    url(r'^listado_auditores/',
        VerAuditores.as_view(),
        name='listado_auditores'),

    url(r'^perfil/',
        include('perfil.urls'), name='perfil'),

    url(r'^revisar_acreditaciones/$',
        'curriculum.views.revisar_acreditaciones',
        name='revisar_acreditaciones'),

    url(r'^revisar_datos/(?P<usuario_id>[\d]+)/',
        login_required(DatosView.as_view()),
        name='requisitos'),

    url(r'^acreditar/(?P<usuario_id>[\d]+)*$',
        login_required(AcreditarView.as_view()),
        name='acreditar'),

    url(r'^fijar_cita/(?P<usuario_id>[\d]+)*$',
        login_required(FijarCitaView.as_view()),
        name='acreditar'),

    url(r'^$',
        TemplateView.as_view(template_name='index.html'),
        name='inicio'),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': os.path.join(os.path.dirname(__file__), 'static')}),
    )
