# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Languaje',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('category', models.ForeignKey(related_name='subcategories', to='caafi.Category', verbose_name='Categoria')),
                ('languaje', models.ManyToManyField(related_name='subcategories', to='caafi.Languaje', verbose_name='Idioma')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('address', models.URLField(verbose_name='Dirección')),
                ('description', models.TextField(default='Escribe una descripción', verbose_name='Descripción')),
                ('primary_competence', models.CharField(max_length=50, verbose_name='Competencia primaria')),
                ('secondary_competence', models.CharField(max_length=50, verbose_name='Competencia secundaria')),
                ('kind_exercise', models.CharField(max_length=50, verbose_name='Tipo de ejercicio')),
                ('level', models.CharField(choices=[('A1', 'A1 - Principiante'), ('A2', 'A2 - Intermedio bajo'), ('B1', 'B1 - Intermedio'), ('B2', 'B2 - Intermedio alto'), ('C1', 'C1 - Avanzado'), ('C2', 'C2 - Perfeccionamiento')], max_length=2, default='---------', verbose_name='Nivel')),
                ('number_items', models.CharField(default='0', max_length=50, verbose_name='Número de items')),
                ('kind_correction', models.CharField(default='Escribe el tipo de correción', max_length=50, verbose_name='Tipo de correción')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('languaje', models.ForeignKey(related_name='urls', to='caafi.Languaje', verbose_name='Idiomas', default=0)),
                ('subcategories', models.ManyToManyField(related_name='urls', to='caafi.Subcategory', verbose_name='Subcategorías')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='category',
            name='languajes',
            field=models.ManyToManyField(related_name='categories', to='caafi.Languaje', verbose_name='Idioma'),
            preserve_default=True,
        ),
    ]
