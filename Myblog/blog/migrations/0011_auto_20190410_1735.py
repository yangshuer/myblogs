# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190410_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textinfo',
            name='text',
            field=models.FileField(verbose_name='正文', upload_to='files'),
        ),
    ]
