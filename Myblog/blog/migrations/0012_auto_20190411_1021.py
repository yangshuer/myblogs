# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20190410_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textinfo',
            name='image',
            field=models.ImageField(verbose_name='标题图片', blank=True, null=True, default=None, upload_to='images'),
        ),
    ]
