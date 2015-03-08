# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('caafi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Nombre', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Nombre', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='url',
            name='kind_item',
            field=models.CharField(verbose_name='Tipo de item', choices=[('EJE', 'Ejemplos'), ('MIN', 'Minutos'), ('PAG', 'Páginas'), ('REA', 'Reactivos'), ('SEG', 'Segundos')], max_length=3, default='---------'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='url',
            name='published',
            field=models.DateTimeField(auto_now_add=True, default=datetime.date(2015, 2, 25)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='url',
            name='kind_correction',
            field=models.CharField(verbose_name='Tipo de correción', choices=[('SI', 'Tiene correción'), ('SI+', 'Tiene correción más explicación'), ('NO', 'No tiene correción'), ('NA', 'No aplica')], max_length=3, default='---------'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='url',
            name='kind_exercise',
            field=models.ForeignKey(related_name='urls', verbose_name='Tipo de ejercicio', to='caafi.Exercise'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='url',
            name='languaje',
            field=models.ForeignKey(related_name='urls', verbose_name='Idioma', default=0, to='caafi.Languaje'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='url',
            name='number_items',
            field=models.IntegerField(verbose_name='Número de items/ Duración'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='url',
            name='primary_competence',
            field=models.ForeignKey(related_name='urls1', verbose_name='Competencia primaria', to='caafi.Competence'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='url',
            name='secondary_competence',
            field=models.ForeignKey(related_name='urls2', verbose_name='Competencia secundaria', to='caafi.Competence'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='url',
            name='status',
            field=models.BooleanField(verbose_name='Disponible', default=True),
            preserve_default=True,
        ),
    ]
