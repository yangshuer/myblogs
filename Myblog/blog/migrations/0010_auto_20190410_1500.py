# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190410_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='imageb',
        ),
        migrations.AddField(
            model_name='textinfo',
            name='image',
            field=models.ImageField(verbose_name='标题图片', blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(verbose_name='图片', blank=True, null=True, upload_to='images'),
        ),
    ]
