# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caafi', '0010_auto_20150331_0539'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='category',
            field=models.ForeignKey(verbose_name='Categoría', related_name='urls1', default=0, to='caafi.Category'),
            preserve_default=True,
        ),
    ]
