# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='wish',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='wish',
            name='product',
        ),
        migrations.RemoveField(
            model_name='wish',
            name='user',
        ),
        migrations.DeleteModel(
            name='Wish',
        ),
    ]
