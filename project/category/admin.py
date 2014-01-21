# -*- coding=utf-8 -*-

from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from category.models import Category, OldCategory
from django.utils.safestring import mark_safe


class CategoryTree(DjangoMpttAdmin):
    pass


class OldCategoryAdmin(admin.ModelAdmin):
    fields = ('category', 'suggestion', 'used', 'cod', 'title', )
    readonly_fields = ('cod', 'title', 'suggestion', 'used', )
    list_display = ('title', 'category', )

    def suggestion(self, obj=None):
        words = obj.title
        for ch in ['(', ')', '[', ']', ';', ':', ',', '.', '-', '_']:
            if ch in words:
                words = (words.replace(ch, ' '))
        matches = []
        for i in words.split():
            if (len(i) > 3):
                if (len(i) < 6 and i[-1] != u's'):
                    matches.append(Category.objects.filter(title__contains=i))
                else:
                    matches.append(Category.objects.filter(
                        title__contains=i[:-2]))
        i_matches = ""
        for i in matches:
            try:
                i_matches = """<a href='javascript:;' data-key='{0}'>
                    {1} </a>""".format(i.get().id, i.get().title)
            except:
                pass
        return mark_safe(i_matches)
    suggestion.short_description = u'Sugestões'

    def used(self, obj=None):
        return this
    used.short_description = u'Semelhantes'


admin.site.register(Category, CategoryTree)
admin.site.register(OldCategory, OldCategoryAdmin)
