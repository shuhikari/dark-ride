#!/usr/bin/env python
# coding=utf-8

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    key =  models.CharField(u'Chave', max_length=255)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    title = models.CharField(u'Título', max_length=255)
    description = models.CharField(u'Descrição', max_length=255)
    qt =  models.IntegerField(u'Quantidade')


class OldCategory(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True)
    cod = models.IntegerField(u'Código')
    title = models.CharField(u'Título', max_length=255)
