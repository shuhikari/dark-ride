#! /usr/bin/env python
# -*- coding=utf-8 -*-

from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from category.models import Category, OldCategory
from django.utils.safestring import mark_safe
from .forms import OldCategoryForm
from django.http import HttpResponse
from datetime import datetime
from django.conf.urls import patterns, url
import unicodecsv as csv


class CategoryTree(DjangoMpttAdmin):
    pass


class OldCategoryAdmin(admin.ModelAdmin):
    form = OldCategoryForm
    fields = ('title', 'category', 'suggestion', 'used', 'cod', 'junk')
    readonly_fields = ('cod', 'title', 'suggestion', 'used', )
    list_display = ('title', 'category', 'junk')

    def suggestion(self, obj=None):
        ws = obj.title
        for ch in ['(', ')', '[', ']', ';', ':', ',', '.', '-', '_']:
            if ch in ws:
                ws = (ws.replace(ch, ' '))
        mt = []
        for i in ws.split():
            if (len(i) > 3):
                if (len(i) < 6 and i[-1]):
                    mt.append(Category.objects.filter(title__contains=i))
                else:
                    mt.append(Category.objects.filter(
                        title__contains=i[:-2]))
        i_mt = ""
        for i in mt:
            try:
                asc = i.get(title=i.get().title)
                for nome in asc.get_ancestors(include_self=True):
                    level = nome.get_level()
                    a = """<a href='javascript:;' data-key='{0}'>{1}</a>"""
                    i_mt += str('|-- ' * level) + a.format(
                        nome.id, nome) + '</br>'

            except:
                pass
        return mark_safe(i_mt)
    suggestion.short_description = u'Sugestões'

    def used(self, obj=None):
        ws = obj.title
        for ch in ['(', ')', '[', ']', ';', ':', ',', '.', '-', '_']:
            if ch in ws:
                ws = (ws.replace(ch, ' '))
        mt = []
        for i in ws.split():
            if (len(i) > 3):
                if (len(i) < 6 and i[-1]):
                    mt.append(OldCategory.objects.filter(title__contains=i))
                else:
                    mt.append(OldCategory.objects.filter(
                        title__contains=i[:-2]))
        i_mt = ""
        for i in mt:
            try:
                a = """<a href='javascript:;' data-key='{0}'>{1} </a>"""
                i_mt = a.format(i.get().id, i.get().title)
            except:
                pass
        return mark_safe(i_mt)
    used.short_description = u'Semelhantes'

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js',
            'js/script.js', 'js/chosen.js',
        )
        css = {
            'all': ('css/chosen.min.css',)
        }

    def csv_export(self, request):
        resp = HttpResponse(content_type='text/csv')
        h = 'attachment; filename="csv_{0}.csv"'
        resp['content-Disposition'] = h.format(datetime.now())
        writer = csv.writer(resp, delimiter=';', quotechar='"')
        for l in OldCategory.objects.all():
            writer.writerow([l.cod, l.title, l.category, l.junk])
        return resp

    def get_urls(self):
        urls = super(OldCategoryAdmin, self).get_urls()
        my_urls = patterns('',
                           url(r'^csv_export/$', self.admin_site.admin_view(
                               self.csv_export), name="csv_export"),
                           )
        return my_urls + urls


admin.site.register(Category, CategoryTree)
admin.site.register(OldCategory, OldCategoryAdmin)
