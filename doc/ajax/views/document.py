"""
Document AJAX Interface
=============================

Description
-----------
Ajax interface routiens

Author : Nik Sumikawa
Date : Feb 11, 2019

"""

import logging

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf.urls import url

from datetime import datetime
from pytz import timezone

from doc import forms, models


def push( request ) :
    """ adds or updates the database entry """

    log = logging.getLogger(__name__)

    log.debug( 'Adding/Updating database entry' )

    idx = request.POST.get('id', 'None')

    form = forms.DocumentForm(request.POST)

    if form.is_valid():
        obj = form.save( request, idx )

        context = { 'id': obj.id,
                    'element_id' : obj.element.id,
                    'name': obj.name,
                    'type': obj.type.name,
                    'link': obj.link,
                    'date': obj.date,
                    'author' : obj.author.username,
                    'error_flag' : False}

    else : context = {'error_flag' : True}

    return JsonResponse(context)

def pull( request ) :
    """ pulls the content from the django database """

    log = logging.getLogger(__name__)

    log.debug( 'pulls the database content for an entry' )

    idx = request.GET.get('id', 'None')

    if idx == 'None' : return JsonResponse({'error_flag':True})

    obj = models.Document.objects.get( id=int(idx), show=True )

    context = { 'id' : idx,
                'name': obj.name,
                'link': obj.link,
                'type': obj.type.id,
                'date': obj.date,
                'element' : obj.element.id,
                'error_flag' : False}


    return JsonResponse(context)


def delete( request ) :
    """ delete the entry from the django database """

    log = logging.getLogger(__name__)

    log.debug( 'delete entry from the database' )

    idx = request.GET.get('id', 'None')

    if idx == 'None' : return JsonResponse({'error_flag':True})

    obj = models.Document.objects.get( id=int(idx) )
    obj.show = False
    obj.save()

    context = { 'id' : idx,
                'error_flag' : False}


    return JsonResponse(context)


def view( request ) :
    """ pulls the content from the django database """

    log = logging.getLogger(__name__)

    log.debug( 'pulls the database content for an entry' )

    idx = request.GET.get('id', 'None')

    if idx == 'None' : return JsonResponse({'error_flag':True})

    doc_obj = models.Document.objects.get( id=int(idx) )

    view_obj = models.View( Document=doc_obj )
    view_obj.save()

    return JsonResponse({})



urlpatterns = [
    url(r'^ajax/views/document/push$', push, name='doc_document_push'),
    url(r'^ajax/views/document/pull$', pull, name='doc_document_pull'),
    url(r'^ajax/views/document/delete$', delete, name='doc_document_delete'),
    url(r'^ajax/views/document/view$', view, name='doc_document_view'),
]
