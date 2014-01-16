#!/usr/bin/env python
# coding=utf-8

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    key =  models.CharField(u'Chave', max_length=255)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children',
                            verbose_name=u'Categoria pai')
    title = models.CharField(u'Título', max_length=255)
    description = models.CharField(u'Descrição', max_length=255)
    qt =  models.IntegerField(u'Quantidade', null=True, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Categoria'
        verbose_name_plural = u'Categorias'


class OldCategory(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, verbose_name="Categoria(fk)")
    cod = models.IntegerField(u'Código')
    title = models.CharField(u'Título', max_length=255)

    class Meta:
        verbose_name = u'Categoria velha'
        verbose_name_plural = u'Categorias velhas'