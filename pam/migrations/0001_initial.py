# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mac_address', models.CharField(default=b'000000000000', help_text=b'Device MAC address', max_length=12)),
                ('description', models.TextField(default=b'', help_text=b'Host')),
                ('last_seen', models.DateTimeField(help_text=b'Date last seen')),
                ('show_in_overview', models.BooleanField(default=True, help_text=b'Show in animation?')),
            ],
        ),
    ]
