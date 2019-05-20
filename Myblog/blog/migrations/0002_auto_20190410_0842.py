# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Block_in', models.CharField(verbose_name='版块', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TextInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='博客标题', max_length=25)),
                ('author', models.CharField(verbose_name='作者', max_length=8)),
                ('introduce', models.TextField(verbose_name='简介', max_length=100)),
                ('text', models.TextField(verbose_name='正文', max_length=5000)),
                ('image', models.ImageField(verbose_name='图片', upload_to='images')),
                ('date', models.DateTimeField(verbose_name='时间', auto_now=True)),
                ('Block', models.ForeignKey(to='blog.BlockInfo')),
            ],
            options={
                'db_table': 'Texttable',
            },
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name='文章正文', blank=True, null=True),
        ),
    ]
