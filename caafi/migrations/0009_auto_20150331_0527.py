# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caafi', '0008_auto_20150331_0514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='category',
            field=models.ForeignKey(to='caafi.Category', default=0, verbose_name='Categoría', related_name='urls1'),
            preserve_default=True,
        ),
    ]
