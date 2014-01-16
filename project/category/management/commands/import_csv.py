#!/usr/bin/env python
# coding=utf-8

import os
from project import settings
from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from category.models import Category


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--csv',
                    dest='csv',
                    help='Informe o nome do arquivo da pasta DOCS, para importar o CSV',
        ),
    )
    def handle(self, csv, **options):
        #import ipdb; ipdb.set_trace();
        if not csv:
            raise CommandError(u'Digite --csv="nome_do_arquivo.csv" : Diretório Base: {0} /docs/'.format(
                settings.BASE_DIR))
        else:
            if not '.csv' in csv:
                csv = csv + '.csv'
            try:
                url = os.path.abspath(os.path.join(settings.BASE_DIR, os.pardir))
                doc_dir = url + '/docs/'
                arquivo = open(doc_dir + csv)
                texto = arquivo.readlines()
                cat = {}
                for idx, linha in enumerate(texto):
                    l = linha.split(',')
                    pai = cat.get(l[1])
                    cat[l[0]] = Category.objects.create(key=str(l[0].replace('"', '')), parent=pai,
                                 title=str(l[2].replace('"', '')),
                                  description=str(l[3].replace('"', '')),
                                  qt=l[4].replace('"', ''))
                    self.stdout.write('Inserindo linha: {0}'.format(str(idx+1)))
            except Exception as e:
                 print e

