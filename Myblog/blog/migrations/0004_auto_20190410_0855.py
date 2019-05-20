# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190410_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textinfo',
            name='Block',
            field=models.ForeignKey(verbose_name='所属版块', to='blog.BlockInfo'),
        ),
    ]
