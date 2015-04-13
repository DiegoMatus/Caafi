# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caafi', '0015_auto_20150413_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(null=True, unique=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(null=True, unique=True, blank=True),
            preserve_default=True,
        ),
    ]
