"""
Search AJAX Interface
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


from doc import forms, models


def get( request ) :
    """ adds or updates the database entry """

    from django.db.models import Q

    log = logging.getLogger(__name__)

    log.debug( 'Searching database' )

    search_field = request.GET.get('search_field', 'None')

    print 'searching!!!!', search_field

    if search_field == 'None' : return JsonResponse({'error_flag' : True})

    element_objects = models.Element.objects.filter(Q(name__icontains = search_field) | \
                                                    Q(description__icontains = search_field) | \
                                                    Q(category__name__icontains = search_field) | \
                                                    Q(category__description__icontains = search_field)
                                                    )


    context = { 'error_flag' : True,
                'elements' : list(element_objects.values_list(  'category__tool__name',
                                                                'category__type__name',
                                                                'category__name',
                                                                'id',
                                                                'name',
                                                                'description'
                                                        ))
                }

    print context
    return JsonResponse(context)


urlpatterns = [
    url(r'^ajax/views/search/get$', get, name='doc_search_get'),
]
