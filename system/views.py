# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

import models as models
import forms as forms
# from .models import Directory, Document, DirectoryTree, FAQ



def profile( request ) :
    """ Development html interface """
    context = {}
    return render(request, 'system/profile.html', context )
