#!/usr/bin/env python
# coding=utf-8

import os
from project import settings
from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from category.models import Category, OldCategory


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--csv',
                    dest='csv',
                    help="""Informe o nome do arquivo da
                    pasta DOCS, para importar o CSV""",
                    ),
    )

    def handle(self, csv, **options):
        #import ipdb; ipdb.set_trace();
        if not csv:
            raise CommandError(u"""Digite --csv="nome_do_arquivo.csv" :
                Diretório Base: {0} /docs/""".format(
                settings.BASE_DIR))
        else:
            if not '.csv' in csv:
                csv = csv + '.csv'
            try:
                url = os.path.abspath(
                    os.path.join(settings.BASE_DIR, os.pardir))
                doc_dir = url + '/docs/'
                arquivo = open(doc_dir + csv)
                texto = arquivo.readlines()
                categories = {}
                for i in Category.objects.all():
                    categories[i.key] = i

                for idx, linha in enumerate(texto):
                    l = linha.split(';')
                    print l[0], l[1]
                    OldCategory.objects.create(
                        category=categories.get(l[2] if len(l) > 3 else ''),
                        cod=int(l[0].replace('"', '')),
                        title=str(l[1].replace('"', '')),
                    )
                    self.stdout.write(
                        'Inserindo linha: {0}'.format(str(idx + 1)))
            except Exception as e:
                print e
