# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 05:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0012_comment_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='upvote_num',
            field=models.IntegerField(default=0),
        ),
    ]
