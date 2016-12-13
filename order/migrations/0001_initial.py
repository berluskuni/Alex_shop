# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20161114_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50, verbose_name='\u0418\u043c\u044f')),
                ('last_name', models.CharField(max_length=50, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('address', models.CharField(max_length=250, verbose_name='\u0410\u0434\u0440\u0435\u0441')),
                ('postal_code', models.CharField(max_length=20, verbose_name='\u041f\u043e\u0447\u0442\u043e\u0432\u044b\u0439 \u043a\u043e\u0434')),
                ('city', models.CharField(max_length=100, verbose_name='\u0413\u043e\u0440\u043e\u0434')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u0421\u043e\u0437\u0434\u0430\u043d')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u041e\u0431\u043d\u043e\u0432\u043b\u0435\u043d')),
                ('paid', models.BooleanField(default=False, verbose_name='\u041e\u043f\u043b\u0430\u0447\u0435\u043d')),
            ],
            options={
                'ordering': ('-created',),
                'db_table': 'db_orders',
                'verbose_name': '\u0417\u0430\u043a\u0430\u0437',
                'verbose_name_plural': '\u0417\u0430\u043a\u0430\u0437\u044b',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.DecimalField(verbose_name='\u0426\u0435\u043d\u0430', max_digits=10, decimal_places=2)),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e')),
                ('order', models.ForeignKey(related_name='items', to='order.Order')),
                ('product', models.ForeignKey(related_name='order_items', to='shop.Product')),
            ],
            options={
                'db_table': 'db_orders_items',
            },
        ),
    ]
