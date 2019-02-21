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

    form = forms.ElementForm(request.POST)
    
    if form.is_valid():
        obj = form.save( idx )

        context = { 'id': obj.id,
                    'category_id' : obj.category.id,
                    'name': obj.name,
                    'description' : obj.description,
                    'error_flag' : False}

    else : context = {'error_flag' : True}

    return JsonResponse(context)

def pull( request ) :
    """ pulls the content from the django database """

    from django.db.models import Q

    log = logging.getLogger(__name__)

    log.debug( 'pulls the database content for an entry' )

    idx = request.GET.get('id', 'None')

    if idx == 'None' : return JsonResponse({'error_flag':True})

    obj = models.Element.objects.get( id=int(idx) )
    document_objects = models.Document.objects.filter(element=obj, show=True)

    #separate the link and template objects
    template_objects = document_objects.filter(Q(type__name = 'Link')|Q(type__name = 'Template'))
    document_objects = document_objects.exclude(Q(type__name = 'Link')|Q(type__name = 'Template'))

    context = { 'id' : idx,
                'name': obj.name,
                'description' : obj.description,
                'category' : obj.category.id,
                'document' : list(document_objects.values_list( 'id',
                                                                'type__name',
                                                                'author__username',
                                                                'link',
                                                                'date',
                                                                'name')),

                'template' : list(template_objects.values_list( 'id',
                                                                'type__name',
                                                                'author__username',
                                                                'link',
                                                                'date',
                                                                'name')),
                'error_flag' : False}

    # print context
    return JsonResponse(context)


def delete( request ) :
    """ delete the entry from the django database """

    log = logging.getLogger(__name__)

    log.debug( 'delete entry from the database' )

    idx = request.GET.get('id', 'None')

    if idx == 'None' : return JsonResponse({'error_flag':True})

    obj = models.Element.objects.get( id=int(idx) )
    obj.show = False
    obj.save()

    context = { 'id' : idx,
                'error_flag' : False}


    return JsonResponse(context)



def get( request ) :
    """ returns all categories based on the specifications """

    from pandas import DataFrame
    log = logging.getLogger(__name__)

    log.debug( 'pulls the database content for an entry' )

    tool = request.GET.get('tool', 'None')
    type = request.GET.get('type', 'None')

    if tool == 'None' or type == 'None' : return JsonResponse({'error_flag':True})

    tool_obj = models.Tool.objects.get( name=tool )
    type_obj = models.Type.objects.get( name=type )

    element_objects = models.Element.objects.filter(category__tool__name=tool_obj,
                                                    category__type__name=type_obj,
                                                    show=True)

    # element_objects = category_objects.element_set
    context = { 'elements' : list(element_objects.values_list(  'category__id',
                                                                'id',
                                                                'name',
                                                                'description')) }


    return JsonResponse(context)



urlpatterns = [
    url(r'^ajax/views/element/push$', push, name='doc_element_push'),
    url(r'^ajax/views/element/pull$', pull, name='doc_element_pull'),
    url(r'^ajax/views/element/delete$', delete, name='doc_element_delete'),
    url(r'^ajax/views/element/get$', get, name='doc_element_get'),
]
