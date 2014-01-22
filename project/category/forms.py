#! /usr/bin/env python
# -*- coding=utf-8 -*-

from django import forms
from .models import OldCategory, Category
from mptt.forms import TreeNodeChoiceField


class OldCategoryForm(forms.ModelForm):
    category = TreeNodeChoiceField(Category.objects.all())

    class Meta:
        model = OldCategory
