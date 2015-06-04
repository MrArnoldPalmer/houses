# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='id',
        ),
        migrations.AlterField(
            model_name='property',
            name='address',
            field=models.TextField(serialize=False, unique=True, primary_key=True),
            preserve_default=True,
        ),
    ]
