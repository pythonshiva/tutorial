# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-27 06:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='style',
            field=models.CharField(choices=[(b'abap', b'abap'), (b'algol', b'algol'), (b'algol_nu', b'algol_nu'), (b'arduino', b'arduino'), (b'autumn', b'autumn'), (b'borland', b'borland'), (b'bw', b'bw'), (b'colorful', b'colorful'), (b'default', b'default'), (b'emacs', b'emacs'), (b'friendly', b'friendly'), (b'fruity', b'fruity'), (b'igor', b'igor'), (b'lovelace', b'lovelace'), (b'manni', b'manni'), (b'monokai', b'monokai'), (b'murphy', b'murphy'), (b'native', b'native'), (b'paraiso-dark', b'paraiso-dark'), (b'paraiso-light', b'paraiso-light'), (b'pastie', b'pastie'), (b'perldoc', b'perldoc'), (b'rainbow_dash', b'rainbow_dash'), (b'rrt', b'rrt'), (b'tango', b'tango'), (b'trac', b'trac'), (b'vim', b'vim'), (b'vs', b'vs'), (b'xcode', b'xcode')], default='friendly', max_length=100),
        ),
    ]
