# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20161114_1013'),
        ('cart', '0002_auto_20161114_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishListProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product', models.ForeignKey(verbose_name='\u0438\u043c\u044f \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0430', blank=True, to='shop.Product', null=True)),
            ],
        ),
    ]
