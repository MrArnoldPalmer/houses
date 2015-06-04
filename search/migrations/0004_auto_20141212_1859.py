# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_auto_20141212_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='property',
        ),
        migrations.DeleteModel(
            name='Data',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='name',
            new_name='address',
        ),
        migrations.AddField(
            model_name='property',
            name='bathrooms',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='property',
            name='bedrooms',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='property',
            name='lot_sq_feet',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='property',
            name='price',
            field=models.DecimalField(max_digits=8, decimal_places=2, default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='property',
            name='sq_feet',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
