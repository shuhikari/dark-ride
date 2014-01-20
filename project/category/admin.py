# -*- coding=utf-8 -*-

from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from category.models import Category, OldCategory


class CategoryTree(DjangoMpttAdmin):
    pass


class OldCategoryAdmin(admin.ModelAdmin):
    fields = ('title', 'category', 'suggestion', 'cod',)
    readonly_fields = ('cod', 'title', 'suggestion', )

    def suggestion(self, obj=None):
        word = u'serviço'
        #TODO: split a frase por espaço e loopar todas que possuem
        # mais de 4 caracteres para usar o filter do ORM
        matches = Category.objects.filter(title__contains=word)
        res = []
        for i in matches:
            #TODO: appendar todas os matches para criar a lista de
            # sugestões. Tentar usar peso contando qual apareceu mais
            # vezes para priorizar. Adicionar o link para selected
            # comparando com a lista de categorias_pga
            res.append(i).__dict__
        return res

    suggestion.short_description = u'Sugestões'

    class Media:
        js = ('js/script.js',)

admin.site.register(Category, CategoryTree)
admin.site.register(OldCategory, OldCategoryAdmin)
