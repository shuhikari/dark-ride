# -*- coding=utf-8 -*-

from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from category.models import Category, OldCategory
from django.utils.safestring import mark_safe


class CategoryTree(DjangoMpttAdmin):
    pass


class OldCategoryAdmin(admin.ModelAdmin):
    fields = ('title', 'category', 'suggestion', 'used', 'cod',)
    readonly_fields = ('cod', 'title', 'suggestion', 'used', )
    list_display = ('title', 'category', )

    def suggestion(self, obj=None):
        ws = obj.title
        for ch in ['(', ')', '[', ']', ';', ':', ',', '.', '-', '_']:
            if ch in ws:
                ws = (ws.replace(ch, ' '))
        mt = []
        for i in ws.split():
            if (len(i) > 3):
                if (len(i) < 6 and i[-1] != u's'):
                    mt.append(Category.objects.filter(title__contains=i))
                else:
                    mt.append(Category.objects.filter(
                        title__contains=i[:-2]))
        i_mt = ""
        for i in mt:
            try:
                i_mt = """<a href='javascript:;' data-key='{0}'>
                    {1} </a>""".format(i.get().id, i.get().title)
            except:
                pass
        return mark_safe(i_mt)
    suggestion.short_description = u'Sugestões'

    def used(self, obj=None):
        return None
    used.short_description = u'Semelhantes'

    class Media:
        js = ('js/script.js',)

admin.site.register(Category, CategoryTree)
admin.site.register(OldCategory, OldCategoryAdmin)
