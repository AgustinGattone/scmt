# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 20:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app.core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfertaDeTrabajo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_trabajo', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='OfertaLaboral',
        ),
    ]
