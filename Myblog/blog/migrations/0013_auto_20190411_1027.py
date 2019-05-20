# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20190411_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textinfo',
            name='image',
            field=models.ImageField(verbose_name='标题图片', blank=True, null=True, default='no', upload_to='images'),
        ),
    ]
