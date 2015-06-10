# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiauth',
            name='users',
            field=models.ManyToManyField(to='api.UserProfile'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='tag',
            field=models.ManyToManyField(to='api.Tag', blank=True),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='defined_partitions',
            field=models.ManyToManyField(to='api.PartitionConfig', verbose_name='\u9884\u5b9a\u4e49\u5206\u533a', blank=True),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='defined_raid_types',
            field=models.ManyToManyField(to='api.RaidConfig', verbose_name='\u9884\u5b9a\u4e49raid\u7c7b\u578b', blank=True),
        ),
        migrations.AlterField(
            model_name='maintainence',
            name='maintain_type',
            field=models.SmallIntegerField(verbose_name='\u53d8\u66f4\u7c7b\u578b', choices=[(1, '\u786c\u4ef6\u66f4\u6362'), (2, '\u65b0\u589e\u914d\u4ef6'), (3, '\u8bbe\u5907\u4e0b\u7ebf'), (4, '\u8bbe\u5907\u4e0a\u7ebf'), (5, '\u5b9a\u671f\u7ef4\u62a4'), (6, '\u4e1a\u52a1\u4e0a\u7ebf\\\u66f4\u65b0\\\u53d8\u66f4'), (7, '\u5176\u5b83')]),
        ),
        migrations.AlterField(
            model_name='nic',
            name='ipaddr',
            field=models.GenericIPAddressField(verbose_name='ip\u5730\u5740'),
        ),
        migrations.AlterField(
            model_name='nicconfig',
            name='gateway',
            field=models.GenericIPAddressField(verbose_name='\u7f51\u5173'),
        ),
        migrations.AlterField(
            model_name='nicconfig',
            name='ipaddr',
            field=models.GenericIPAddressField(verbose_name='ip\u5730\u5740'),
        ),
    ]
