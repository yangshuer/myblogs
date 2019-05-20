# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190410_0842'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='blockinfo',
            table='BlockInfo',
        ),
    ]
