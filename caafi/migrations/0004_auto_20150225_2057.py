# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('caafi', '0003_auto_20150225_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='published',
            field=models.DateTimeField(auto_now_add=True, default=datetime.date(2015, 2, 25)),
            preserve_default=True,
        ),
    ]
