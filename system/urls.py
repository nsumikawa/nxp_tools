from django.conf.urls import url

from . import views
from ajax.views import category, element, document

urlpatterns = [
    # ex: /
    url(r'^profile/$', views.profile, name='profile'),
]
