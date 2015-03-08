# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caafi', '0006_attendant'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Languaje',
            new_name='Language',
        ),
        migrations.RenameField(
            model_name='attendant',
            old_name='languaje',
            new_name='language',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='languajes',
            new_name='languages',
        ),
        migrations.RenameField(
            model_name='subcategory',
            old_name='languaje',
            new_name='language',
        ),
        migrations.RenameField(
            model_name='url',
            old_name='languaje',
            new_name='language',
        ),
    ]
