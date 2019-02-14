from django.conf.urls import url

from . import views
from ajax.views import category, element, document

urlpatterns = [
    # ex: /
    url(r'^$', views.test, name='test'),
    # url(r'^$', views.training_doc, name='training_doc'),
    # url(r'^training_doc/$', views.training_doc, name='training_doc'),
    # url(r'^training_doc/(?P<dir_id>[0-9]+)/$', views.training_doc, name='training_doc'),
    #
    #
    # url(r'^add_doc/$', views.update_document, name='add_doc'),
    # url(r'^add_doc/(?P<event_id>[0-9]+)/$', views.update_document, name='add_doc'),
    #
    #
    # url(r'^search/$', views.search, name='search'),
    # url(r'^new_documents/$', views.new_documents, name='new_documents'),
    #
    #
    # url(r'^training_faq/$', views.training_faq, name='training_faq'),
    # url(r'^training_faq/(?P<dir_id>[0-9]+)/$', views.training_faq, name='training_faq'),
    # url(r'^add_faq/$', views.update_FAQ, name='add_faq'),
    # url(r'^add_faq/(?P<event_id>[0-9]+)/$', views.update_FAQ, name='add_faq'),
]

urlpatterns += category.urlpatterns
urlpatterns += element.urlpatterns
urlpatterns += document.urlpatterns
