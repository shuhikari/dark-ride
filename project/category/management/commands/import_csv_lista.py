#!/usr/bin/env python
# coding=utf-8

import os
import csv
from project import settings
from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from category.models import Category, OldCategory


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--csv',
                    dest='csv_file',
                    help="""Informe o nome do arquivo da
                    pasta DOCS, para importar o CSV""",
                    ),
    )

    def handle(self, csv_file, **options):
        if not csv_file:
            raise CommandError(u"""Digite --csv="nome_do_arquivo.csv" :
                Diretório Base: {0} /docs/""".format(
                settings.BASE_DIR))
        else:
            if not '.csv' in csv_file:
                csv_file = csv_file + '.csv'
            try:
                url = os.path.abspath(
                    os.path.join(settings.BASE_DIR, os.pardir))
                doc_dir = url + '/docs/'
                with open(doc_dir + csv_file, 'rb') as arquivo:
                    spam_csv = csv.reader(
                        arquivo, delimiter=';', quotechar='"')
                    cat = {}
                    lines = [i for i in spam_csv]
                    OldCat = {}
                    for i in Category.objects.all():
                        cat[i.key] = i
                    for i in lines:
                        if len(i) > 2 and len(i[2]) > 11:
                            OldCat[i[2]] = i[2]
                    for idx, l in enumerate(lines):
                        OldCategory.objects.create(
                            category=cat.get(l[2] if len(l) > 2 else ''),
                            cod=int(l[0]),
                            title=str(l[1]),
                            junk=OldCat.get(l[2] if len(l) > 2 else ''),
                        )
                        self.stdout.write(
                            'Inserindo linha: {0}'.format(str(idx + 1))
                        )
            except Exception as e:
                print e
