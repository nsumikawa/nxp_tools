from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^doc/', include('doc.urls', namespace="doc")),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
