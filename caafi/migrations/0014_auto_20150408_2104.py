# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('caafi', '0013_remove_language_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='slug',
            field=models.SlugField(null=True, blank=True, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='url',
            name='published',
            field=models.DateTimeField(auto_now_add=True, default=datetime.date(2015, 4, 8)),
            preserve_default=True,
        ),
    ]
