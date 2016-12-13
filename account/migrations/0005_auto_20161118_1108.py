# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_user_city'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='country',
            new_name='country_id',
        ),
    ]
