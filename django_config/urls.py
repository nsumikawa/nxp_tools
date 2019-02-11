from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^doc/', include('doc.urls', namespace="doc")),

    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls', namespace="auth")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
