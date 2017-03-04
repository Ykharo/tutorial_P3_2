# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-01 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0006_auto_20160925_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='edp',
            name='PersComAltoCarmen',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=21, null=True),
        ),
        migrations.AddField(
            model_name='edp',
            name='PersComFreirina',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=21, null=True),
        ),
        migrations.AddField(
            model_name='edp',
            name='PersComHuasco',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=21, null=True),
        ),
        migrations.AddField(
            model_name='edp',
            name='PersComVallenar',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=21, null=True),
        ),
        migrations.AddField(
            model_name='edp',
            name='PersHombres',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=21, null=True),
        ),
        migrations.AddField(
            model_name='edp',
            name='PersLocal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=21, null=True),
        ),
        migrations.AddField(
            model_name='edp',
            name='PersMujeres',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=21, null=True),
        ),
        migrations.AddField(
            model_name='edp',
            name='PersNoLocal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=21, null=True),
        ),
    ]