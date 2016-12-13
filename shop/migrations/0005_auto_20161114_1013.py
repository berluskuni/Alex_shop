# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(default=b'', max_length=40, verbose_name='\u0426\u0432\u0435\u0442', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(default=b'', max_length=10, verbose_name='\u0420\u0430\u0437\u043c\u0435\u0440', blank=True),
        ),
    ]
