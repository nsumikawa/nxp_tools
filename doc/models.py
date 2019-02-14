"""
Models
======

Description
-----------
documentation Model defition

Author : Nik Sumikawa
Date : Feb 8, 2019
"""

from django.db import models
from django.conf import settings
# Create your models here.

class Tool(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Type(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):

    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.name


class Element(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.name


class DocumentType( models.Model ):

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.name

class Document(models.Model):

    element = models.ForeignKey(Element)
    type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)

    date = models.DateTimeField('date published', auto_now=True, null=True, blank=True)
    author = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                null=True, blank=True)

    name = models.CharField(max_length=200)
    link = models.CharField(max_length=5000, blank=True, null=True)

    def __str__(self):
        return self.name


class View(models.Model):

    Document = models.ForeignKey(Document)
    date = models.DateTimeField('date viewed')


# class DirectoryTree(models.Model):
#
#     parent = models.ForeignKey(Directory, on_delete=models.CASCADE, blank=True, null=True)
#
#     name = models.CharField(max_length=200)
#
#     def __unicode__(self):
#         return self.name
#
#
# class Document(models.Model):
#
#     directory = models.ForeignKey(Directory)
#
#     date = models.DateTimeField('date published', null=True, blank=True)
#     name = models.CharField(max_length=200)
#     description = models.CharField(max_length=2000, blank=True, null=True)
#     pptx_href = models.CharField(max_length=2000, blank=True, null=True)
#     video_href = models.CharField(max_length=2000, blank=True, null=True)
#
#
#     def __unicode__(self):
#         return self.name
#
#
# class FAQ(models.Model):
#
#     directory = models.ForeignKey(Directory)
#
#     date = models.DateTimeField('date published', null=True, blank=True)
#     question = models.CharField(max_length=1000)
#     answer = models.CharField(max_length=5000, blank=True, null=True)
#     pptx_href = models.CharField(max_length=2000, blank=True, null=True)
#     video_href = models.CharField(max_length=2000, blank=True, null=True)
#     img_href = models.CharField(max_length=2000, blank=True, null=True)
#
#
#     def __unicode__(self):
#         return self.question
