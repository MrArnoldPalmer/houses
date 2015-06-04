# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('address', models.TextField()),
                ('price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.DecimalField(max_digits=2, decimal_places=1)),
                ('sq_feet', models.IntegerField()),
                ('lot_sq_ft', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
