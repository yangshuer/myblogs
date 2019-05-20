# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190410_0858'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('image', models.ImageField(verbose_name='图片', blank=True, null=True, upload_to='images')),
            ],
        ),
        migrations.RemoveField(
            model_name='textinfo',
            name='image',
        ),
        migrations.AddField(
            model_name='images',
            name='Text',
            field=models.ForeignKey(verbose_name='所属文章', to='blog.TextInfo'),
        ),
    ]
