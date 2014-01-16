from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from category.models import Category, OldCategory

class CategoryTree(DjangoMpttAdmin):
    pass

admin.site.register(Category, CategoryTree)
admin.site.register(OldCategory)
