# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


# class Directory(models.Model):
#
#     name = models.CharField(max_length=200)
#     description = models.CharField(max_length=2000, blank=True, null=True)
#
#     def __unicode__(self):
#         return self.name
#
#
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
