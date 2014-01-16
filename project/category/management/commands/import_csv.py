#!/usr/bin/env python
# coding=utf-8

import os
from project import settings as base
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
            return u'Digite --csv="nome_do_arquivo.csv" : Diretório Base: ' + base.BASE_DIR + '/docs/'
        else:
            if not '.csv' in csv:
                csv = csv + '.csv'
            try:
                url = os.path.abspath(os.path.join(base.BASE_DIR, os.pardir))
                doc_dir = url + '/docs/'
                arquivo = open(doc_dir + csv)
                texto = arquivo.readlines()
                for idx, linha in enumerate(texto):
                    l = linha.split(',')
                    if not l[1]:
                        pai = Category.objects.create(key=l[0].replace('"', ''), qt=l[4].replace('"', ''))
                    else:
                        pai = Category.objects.create(key=l[1].replace('"', ''), qt=l[4].replace('"', ''))
                    insere = Category(key=str(l[0].replace('"', '')), parent=pai,
                             title=str(l[2].replace('"', '')),
                              description=str(l[3].replace('"', '')),
                              qt=l[4].replace('"', ''))
                    insere.save()
                    print 'Inserindo registro: ' + l[0] + ' indice: ' str(idx + 1)
            except Exception as e:
                 print e

