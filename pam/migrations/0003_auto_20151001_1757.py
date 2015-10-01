# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pam', '0002_device_currently_in_space'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='currently_in_space',
            field=models.BooleanField(default=False, help_text=b'Currently in the space?', editable=False),
        ),
        migrations.AlterField(
            model_name='device',
            name='description',
            field=models.CharField(default=b'', help_text=b'Host', max_length=42),
        ),
    ]
