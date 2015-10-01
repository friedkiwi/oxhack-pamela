# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='currently_in_space',
            field=models.BooleanField(default=False, help_text=b'Currently in the space?'),
        ),
    ]
