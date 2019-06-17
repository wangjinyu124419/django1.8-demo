# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='push_entire',
            field=models.BooleanField(default=True, help_text=b'Push To All Users'),
        ),
        migrations.AlterField(
            model_name='question',
            name='year_in_school',
            field=models.CharField(max_length=2, choices=[(b'f', b'Freshman'), (b's', b'Sophomore')]),
        ),
    ]
