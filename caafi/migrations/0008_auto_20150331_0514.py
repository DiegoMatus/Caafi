# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('caafi', '0007_auto_20150227_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='category',
            field=models.ForeignKey(related_name='urls1', default='---------', verbose_name='Categoría', to='caafi.Category'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='url',
            name='primary_competence',
            field=models.ForeignKey(related_name='urls3', to='caafi.Competence', verbose_name='Competencia primaria'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='url',
            name='published',
            field=models.DateTimeField(auto_now_add=True, default=datetime.date(2015, 3, 31)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='url',
            name='secondary_competence',
            field=models.ForeignKey(related_name='urls4', to='caafi.Competence', verbose_name='Competencia secundaria'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='url',
            name='subcategories',
            field=models.ManyToManyField(verbose_name='Subcategorías', related_name='urls2', to='caafi.Subcategory'),
            preserve_default=True,
        ),
    ]
