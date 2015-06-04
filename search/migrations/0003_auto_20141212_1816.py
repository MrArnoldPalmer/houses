# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20141212_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('address', models.TextField(primary_key=True, unique=True, serialize=False)),
                ('price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.DecimalField(max_digits=2, decimal_places=1)),
                ('sq_feet', models.IntegerField()),
                ('lot_sq_ft', models.IntegerField()),
                ('property', models.ForeignKey(to='search.Property')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='property',
            old_name='address',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='property',
            name='bathrooms',
        ),
        migrations.RemoveField(
            model_name='property',
            name='bedrooms',
        ),
        migrations.RemoveField(
            model_name='property',
            name='lot_sq_ft',
        ),
        migrations.RemoveField(
            model_name='property',
            name='price',
        ),
        migrations.RemoveField(
            model_name='property',
            name='sq_feet',
        ),
    ]
