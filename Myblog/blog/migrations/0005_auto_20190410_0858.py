# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190410_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textinfo',
            name='image',
            field=models.ImageField(verbose_name='图片', blank=True, null=True, upload_to='images'),
        ),
    ]
