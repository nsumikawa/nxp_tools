from django.conf.urls import url

from . import views
from ajax.views import category, element, document, search

urlpatterns = [
    # ex: /
    url(r'^$', views.test, name='test'),
    url(r'^broken/$', views.broken, name='broken'),

]

urlpatterns += category.urlpatterns
urlpatterns += element.urlpatterns
urlpatterns += document.urlpatterns
urlpatterns += search.urlpatterns
