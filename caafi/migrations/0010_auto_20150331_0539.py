# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caafi', '0009_auto_20150331_0527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='category',
        ),
        migrations.AlterField(
            model_name='url',
            name='kind_exercise',
            field=models.ForeignKey(verbose_name='Tipo de ejercicio', to='caafi.Exercise', related_name='urls5'),
            preserve_default=True,
        ),
    ]
