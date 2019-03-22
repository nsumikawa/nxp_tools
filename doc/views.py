# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

import models as models
import forms as forms
# from .models import Directory, Document, DirectoryTree, FAQ



def test( request ) :
    """ Development html interface """

    context = { 'category_form': forms.CategoryForm(),
                'document_form': forms.DocumentForm(),
                'element_form': forms.ElementForm(),
                }
    return render(request, 'doc/landing.html', context )


def broken( request ) :
    """ Development html interface """

    return render(request, 'doc/broken.html' )
