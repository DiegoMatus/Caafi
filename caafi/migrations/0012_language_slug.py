# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('caafi', '0011_url_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 3, 31, 7, 44, 26, 778789, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
