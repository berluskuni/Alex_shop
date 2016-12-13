# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=250, null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441', blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=100, null=True, verbose_name='\u0413\u043e\u0440\u043e\u0434', blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(max_length=50, null=True, verbose_name='\u0418\u043c\u044f', blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(max_length=50, null=True, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f', blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='postal_code',
            field=models.CharField(max_length=20, null=True, verbose_name='\u041f\u043e\u0447\u0442\u043e\u0432\u044b\u0439 \u043a\u043e\u0434', blank=True),
        ),
    ]
