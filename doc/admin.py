# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

class ToolAdmin(admin.ModelAdmin):
    model = Tool
    list_display = ('name', )

class TypeAdmin(admin.ModelAdmin):
    model = Type
    list_display = ('name', )

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('tool', 'type', 'name' )
    list_filter = ['name']
    search_fields = ['name']


class ElementAdmin(admin.ModelAdmin):
    model = Element
    list_display = ('category', 'name' )
    list_filter = ['name']
    search_fields = ['name']

class DocumentTypeAdmin(admin.ModelAdmin):
    model = DocumentType
    list_display = ('name', )
    list_filter = ['name']
    search_fields = ['name']


class DocumentAdmin(admin.ModelAdmin):
    model = Document
    list_display = ('element','type','date','author','name', 'link' )
    list_filter = ['name']
    search_fields = ['name']


class ViewAdmin(admin.ModelAdmin):
    model = View
    list_display = ('date',)
    list_filter = ['date']
    search_fields = ['date']

admin.site.register(Tool, ToolAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Element, ElementAdmin)
admin.site.register(DocumentType, DocumentTypeAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(View, ViewAdmin)
