"""
Category AJAX Interface
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

    form = forms.CategoryForm(request.POST)

    if form.is_valid():
        obj = form.save( idx )
        
        context = { 'id' : obj.id,
                    'name': obj.name,
                    'description' : obj.description,
                    'error_flag' : False}

    else : context = {'error_flag' : True}

    return JsonResponse(context)

def pull( request ) :
    """ pulls the content from the django database """

    log = logging.getLogger(__name__)

    log.debug( 'pulls the database content for an entry' )

    idx = request.GET.get('id', 'None')

    if idx == 'None' : return JsonResponse({'error_flag':True})

    obj = models.Category.objects.get( id=idx )
    element_objects = models.Element.objects.filter( category=obj )

    context = { 'id' : idx,
                'name': obj.name,
                'description' : obj.description,
                'tool' : obj.tool.id,
                'type' : obj.type.id,
                'elements' : list(element_objects.values_list('id', 'name', 'description')),
                'error_flag' : False}


    return JsonResponse(context)


def delete( request ) :
    """ delete the entry from the django database """

    log = logging.getLogger(__name__)

    log.debug( 'delete entry from the database' )

    idx = request.GET.get('id', 'None')

    if idx == 'None' : return JsonResponse({'error_flag':True})

    category_obj = models.Category( id=int(idx) )
    category_obj.delete()

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

    category_objects = models.Category.objects.filter( tool=tool_obj, type=type_obj )

    att_list = ['name', 'description']

    context = { 'categories' : list(category_objects.values_list('id', 'name', 'description')) }

    print context
    return JsonResponse(context)



urlpatterns = [
    url(r'^ajax/views/category/push$', push, name='doc_category_push'),
    url(r'^ajax/views/category/pull$', pull, name='doc_category_pull'),
    url(r'^ajax/views/category/delete$', delete, name='doc_category_delete'),
    url(r'^ajax/views/category/get$', get, name='doc_category_get'),
]
