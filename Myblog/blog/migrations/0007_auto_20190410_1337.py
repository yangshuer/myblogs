# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190410_1336'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='images',
            table='Images',
        ),
    ]
