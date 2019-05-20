# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190410_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='imageb',
            field=models.ImageField(verbose_name='图片', blank=True, null=True, upload_to='images'),
        ),
    ]
