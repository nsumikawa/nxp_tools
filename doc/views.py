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
    return render(request, 'doc/test.html', context )

# def training_doc(request, dir_id=None):
#
#     if dir_id != None :
#         directory = get_object_or_404(Directory, pk=dir_id)
#     else : directory = Directory.objects.get( name='root' )
#
#     context = { 'dir_name':directory,
#                 'page_type':'DOC' }
#
#     temp = directory.directorytree_set.all()
#     if len( temp ) > 0 :
#         names = [obj.name for obj in temp]
#         dir_tree = Directory.objects.filter( name__in=names )
#         context['dir_tree'] = dir_tree
#
#     documents = Document.objects.filter(directory=dir_id)
#     if len(documents) > 0 : context['documents'] = documents
#
#     return render(request, 'training/training_doc.html', context)
#
#
# def search( request ) :
#     """ searches through the documents and directory structure for key words """
#
#     from itertools import chain
#
#     #retrieve the contents from the search field
#     search_field = request.POST.get('search', '/')
#
#     # from training.models import Document
#     context = {'page_type':'BOTH'}
#
#     context['dir_tree'] = Directory.objects.filter(name__icontains=search_field)
#     doc = Document.objects.filter(description__icontains=search_field)
#     faq = FAQ.objects.filter(answer__icontains=search_field)
#
#     context['documents'] = list(chain(doc, faq))
#
#     return render(request, 'training/training_doc.html', context)
#


# def new_documents( request ) :
#     """ returns a list of most recently added documents """
#
#     from itertools import chain
#
#     new_doc = Document.objects.order_by('-date')[:10]
#     new_faq = FAQ.objects.order_by('-date')[:10]
#
#     context = {'page_type':'BOTH'}
#     context['documents'] = list(chain(new_doc, new_faq))
#
#     return render(request, 'training/training_doc.html', context)
#
#
#
# def update_document( request, event_id=None ) :
#     """ routine for updating event model """
#
#     from .forms import DocumentForm
#     from .models import Document
#
#     form = DocumentForm(request.POST)
#
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect(reverse('training:training_doc'))
#
#     elif event_id != None :
#         doc = Document.objects.get(pk=event_id)
#         print doc.directory.description
#         init_d = {'name':doc.name, 'directory':doc.directory, 'description':doc.description,
#                 'pptx_href':doc.pptx_href, 'video_href':doc.video_href}
#         form = DocumentForm(initial=init_d)
#
#
#     else : form = DocumentForm()
#
#     return render(request, 'training/add_doc.html', {'form':form})
#
#
#
#
# def training_faq(request, dir_id=None):
#
#     if dir_id != None :
#         directory = get_object_or_404(Directory, pk=dir_id)
#     else : directory = Directory.objects.get( name='faq_root' )
#
#     context = { 'dir_name':directory,
#                 'page_type':'FAQ'}
#
#     temp = directory.directorytree_set.all()
#     if len( temp ) > 0 :
#         names = [obj.name for obj in temp]
#         dir_tree = Directory.objects.filter( name__in=names )
#         context['dir_tree'] = dir_tree
#
#     documents = FAQ.objects.filter(directory=dir_id)
#     if len(documents) > 0 : context['documents'] = documents
#
#     print context
#     return render(request, 'training/training_doc.html', context)
#
#
# def update_FAQ( request, event_id=None ) :
#     """ routine for adding/updating FAQ """
#
#     from .forms import FAQForm
#     from .models import FAQ
#
#     form = FAQForm(request.POST)
#
#     # print 'is form valid?', form.is_valid(), form
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect(reverse('training:training_faq'))
#
#     elif event_id != None :
#         doc = FAQ.objects.get(pk=event_id)
#         init_d = {  'question':doc.question,
#                     'directory':doc.directory,
#                     'answer':doc.answer,
#                     'pptx_href':doc.pptx_href,
#                     'video_href':doc.video_href,
#                     'img_href':doc.img_href,
#                     }
#         form = FAQForm(initial=init_d)
#
#
#     else : form = FAQForm()
#
#     return render(request, 'training/add_faq.html', {'form':form})
