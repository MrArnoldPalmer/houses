# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0005_auto_20141212_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='distance_to_bar',
            field=models.DecimalField(default=0, max_digits=3, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='property',
            name='distance_to_public_transit',
            field=models.DecimalField(default=0, max_digits=3, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='property',
            name='home_type',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='image_url',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='proximity_to_volcanoe',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='property',
            name='school_rating',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
