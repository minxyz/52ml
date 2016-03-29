from django.conf.urls import url, include
from django.contrib import admin
from django.views.i18n import set_language


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('apps.core.urls', namespace='core')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
	url(r'^i18n/setlang/$', set_language, name='set_language'),
]
