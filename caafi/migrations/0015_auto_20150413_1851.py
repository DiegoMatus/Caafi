# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('caafi', '0014_auto_20150408_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='published',
            field=models.DateTimeField(auto_now_add=True, default=datetime.date(2015, 4, 13)),
            preserve_default=True,
        ),
    ]
