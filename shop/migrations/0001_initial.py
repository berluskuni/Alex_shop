# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, db_index=True)),
                ('slug', models.SlugField(unique=True, max_length=200)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435', db_index=True)),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(upload_to=b'product/%Y/%m/%d', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u0442\u043e\u0432\u0430\u0440\u0430', blank=True)),
                ('description', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430', blank=True)),
                ('price', models.DecimalField(verbose_name='\u0426\u0435\u043d\u0430 \u0442\u043e\u0432\u0430\u0440\u0430', max_digits=10, decimal_places=2)),
                ('stock', models.PositiveIntegerField(verbose_name='\u041d\u0430 \u0441\u043a\u043b\u0430\u0434\u0435')),
                ('available', models.BinaryField(default=True, verbose_name='\u0414\u043e\u0441\u0442\u0443\u043f\u0435\u043d')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(related_name='product', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', to='shop.Category')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, db_index=True)),
                ('slug', models.SlugField(unique=True, max_length=200)),
                ('categories', models.ForeignKey(related_name='subcategory', to='shop.Category')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '\u041f\u043e\u0434 \u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
                'verbose_name_plural': '\u041f\u043e\u0434 \u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(related_name='product', verbose_name='\u041f\u043e\u0434\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', to='shop.SubCategory'),
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together=set([('id', 'slug')]),
        ),
    ]
