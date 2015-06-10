# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiAuth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=64, verbose_name='\u63a5\u53e3url')),
                ('description', models.CharField(max_length=64, verbose_name='\u7b80\u4ecb')),
                ('method_type', models.CharField(max_length=32, verbose_name='\u53ef\u7528\u65b9\u6cd5', choices=[(b'GET', b'\xe5\x85\x81\xe8\xae\xb8Get(\xe5\x8f\xaf\xe8\xaf\xbb)'), (b'POST', b'\xe5\x85\x81\xe8\xae\xb8POST(\xe5\x8f\xaf\xe4\xbf\xae\xe6\x94\xb9)'), (b'PUT', b'\xe5\x85\x81\xe8\xae\xb8PUT(\xe5\x8f\xaf \xe5\x88\x9b\xe5\xbb\xba)'), (b'HEAD', b'HEAD(\xe6\x9a\x82\xe4\xb8\x8d\xe7\x94\xa8)'), (b'PATCH', b'PATCH(\xe6\x9a\x82\xe4\xb8\x8d\xe7\x94\xa8)')])),
            ],
            options={
                'verbose_name': '\u63a5\u53e3\u6743\u9650',
                'verbose_name_plural': '\u63a5\u53e3\u6743\u9650',
            },
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('device_type', models.CharField(default=b'server', max_length=64, choices=[(b'server', '\u670d\u52a1\u5668'), (b'switch', '\u4ea4\u6362\u673a'), (b'router', '\u8def\u7531\u5668'), (b'firewall', '\u9632\u706b\u5899'), (b'storage', '\u5b58\u50a8\u8bbe\u5907'), (b'NLB', 'NetScaler')])),
                ('name', models.CharField(max_length=30)),
                ('hostname', models.CharField(unique=True, max_length=64, blank=True)),
                ('trade_time', models.DateField(null=True, verbose_name='\u8d2d\u4e70\u65f6\u95f4', blank=True)),
                ('expire_time', models.DateField(null=True, verbose_name='\u8fc7\u4fdd\u65f6\u95f4', blank=True)),
                ('warranty', models.SmallIntegerField(null=True, verbose_name='\u4fdd\u4fee\u671f', blank=True)),
                ('price', models.FloatField(null=True, verbose_name='\u4ef7\u683c', blank=True)),
                ('function', models.CharField(max_length=32, null=True, blank=True)),
                ('cabinet_num', models.CharField(max_length=30, null=True, verbose_name='\u673a\u67dc\u53f7', blank=True)),
                ('cabinet_order', models.SmallIntegerField(null=True, verbose_name='\u673a\u67dc\u4e2d\u5e8f\u53f7', blank=True)),
                ('memo', models.TextField(null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u8d44\u4ea7\u603b\u8868',
                'verbose_name_plural': '\u8d44\u4ea7\u603b\u8868',
            },
        ),
        migrations.CreateModel(
            name='AssetStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('os_installed', models.BooleanField(default=False)),
                ('puppet_installed', models.BooleanField(default=False)),
                ('zabbix_configured', models.BooleanField(default=False)),
                ('auditing_configured', models.BooleanField(default=False)),
                ('approved', models.BooleanField(default=False)),
                ('asset', models.OneToOneField(to='api.Asset')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessUnit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64, verbose_name='\u4e1a\u52a1\u7ebf')),
                ('memo', models.CharField(max_length=64, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'verbose_name': '\u4e1a\u52a1\u7ebf',
                'verbose_name_plural': '\u4e1a\u52a1\u7ebf',
            },
        ),
        migrations.CreateModel(
            name='BusinessUnitLevel2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64, verbose_name='\u4e8c\u7ea7\u4e1a\u52a1\u7ebf')),
                ('memo', models.CharField(max_length=64, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'verbose_name': '\u4e8c\u7ea7\u4e1a\u52a1\u7ebf',
                'verbose_name_plural': '\u4e8c\u7ea7\u4e1a\u52a1\u7ebf',
            },
        ),
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('management_ip', models.CharField(max_length=64, null=True, verbose_name='\u7ba1\u7406IP', blank=True)),
                ('business_ip', models.CharField(max_length=64, null=True, verbose_name='\u4e1a\u52a1IP', blank=True)),
                ('business_netmask', models.CharField(max_length=64, null=True, verbose_name='\u5b50\u7f51\u63a9\u7801', blank=True)),
                ('business_gateway', models.CharField(max_length=64, null=True, verbose_name='\u4e1a\u52a1\u7f51\u5173', blank=True)),
                ('vlan_id', models.SmallIntegerField(null=True, blank=True)),
                ('os_install_zone', models.CharField(default=b'bj', max_length=32, verbose_name='PXE\u670d\u52a1\u6240\u5728\u673a\u623f', choices=[(b'bj', '\u5317\u4eac\u5146\u7ef4'), (b'sjz', '\u77f3\u5bb6\u5e84'), (b'lq', '\u77f3\u5bb6\u5e84\u9e7f\u6cc9')])),
                ('asset', models.OneToOneField(default=None, to='api.Asset')),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sn', models.CharField(unique=True, max_length=64, verbose_name='\u5408\u540c\u53f7')),
                ('name', models.CharField(max_length=64, verbose_name='\u5408\u540c\u540d\u79f0')),
                ('memo', models.TextField(verbose_name='\u5907\u6ce8', blank=True)),
                ('cost', models.IntegerField(verbose_name='\u5408\u540c\u91d1\u989d')),
                ('start_date', models.DateTimeField(blank=True)),
                ('end_date', models.DateTimeField(blank=True)),
                ('license_num', models.IntegerField(verbose_name='license\u6570\u91cf', blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u5408\u540c',
                'verbose_name_plural': '\u5408\u540c',
            },
        ),
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sn', models.CharField(max_length=64, verbose_name='SN\u53f7', blank=True)),
                ('parent_sn', models.CharField(unique=True, max_length=128, blank=True)),
                ('manufactory', models.CharField(default=None, max_length=32, verbose_name='\u5236\u9020\u5546', blank=True)),
                ('model', models.CharField(max_length=64, verbose_name='CPU\u578b\u53f7', blank=True)),
                ('memo', models.TextField(verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'verbose_name': 'CPU\u90e8\u4ef6',
                'verbose_name_plural': 'CPU\u90e8\u4ef6',
            },
        ),
        migrations.CreateModel(
            name='Disk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sn', models.CharField(max_length=128, verbose_name='SN\u53f7', blank=True)),
                ('parent_sn', models.CharField(max_length=128, blank=True)),
                ('slot', models.CharField(max_length=32, verbose_name='\u63d2\u69fd\u4f4d', blank=True)),
                ('enclosure', models.CharField(max_length=128, null=True, blank=True)),
                ('manufactory', models.CharField(default=None, max_length=32, verbose_name='\u5236\u9020\u5546', blank=True)),
                ('model', models.CharField(max_length=128, verbose_name='\u78c1\u76d8\u578b\u53f7', blank=True)),
                ('capacity', models.FloatField(verbose_name='\u78c1\u76d8\u5bb9\u91cfGB', blank=True)),
                ('iface_type', models.CharField(blank=True, max_length=64, verbose_name='\u63a5\u53e3\u7c7b\u578b', choices=[(b'SATA', b'SATA'), (b'SAS', b'SAS'), (b'SCSI', b'SCSI'), (b'SSD', b'SSD')])),
                ('memo', models.TextField(verbose_name='\u5907\u6ce8', blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u786c\u76d8\u90e8\u4ef6',
                'verbose_name_plural': '\u786c\u76d8\u90e8\u4ef6',
            },
        ),
        migrations.CreateModel(
            name='DiskConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sn', models.CharField(max_length=128, null=True, verbose_name='SN\u53f7', blank=True)),
                ('parent_sn', models.CharField(max_length=128, null=True, blank=True)),
                ('slot', models.CharField(max_length=32, null=True, verbose_name='\u63d2\u69fd\u4f4d', blank=True)),
                ('memo', models.TextField(null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.CharField(unique=True, max_length=128, verbose_name='\u8bf7\u6c42ID')),
                ('post_data', models.TextField(verbose_name='\u8bf7\u6c42Data', blank=True)),
                ('detail', models.TextField(verbose_name='\u8be6\u7ec6\u63cf\u8ff0', blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u673a\u623fenglish')),
                ('display_name', models.CharField(default=None, max_length=32, verbose_name='\u4e2d\u6587\u663e\u793a\u540d')),
                ('region', models.CharField(default=None, max_length=64, verbose_name='\u533a\u57df')),
                ('region_display_name', models.CharField(default=None, max_length=64, verbose_name='\u533a\u57df\u4e2d\u6587')),
                ('isp', models.CharField(default=None, max_length=32, verbose_name='\u8fd0\u8425\u5546')),
                ('isp_display_name', models.CharField(default=None, max_length=32, verbose_name='\u8fd0\u8425\u5546\u4e2d\u6587')),
                ('floor', models.IntegerField(default=1, verbose_name='\u697c\u5c42')),
                ('memo', models.CharField(max_length=64, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '\u673a\u623f',
                'verbose_name_plural': '\u673a\u623f',
            },
        ),
        migrations.CreateModel(
            name='Maintainence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u4e8b\u4ef6\u540d\u79f0')),
                ('maintain_type', models.SmallIntegerField(max_length=30, verbose_name='\u53d8\u66f4\u7c7b\u578b', choices=[(1, '\u786c\u4ef6\u66f4\u6362'), (2, '\u65b0\u589e\u914d\u4ef6'), (3, '\u8bbe\u5907\u4e0b\u7ebf'), (4, '\u8bbe\u5907\u4e0a\u7ebf'), (5, '\u5b9a\u671f\u7ef4\u62a4'), (6, '\u4e1a\u52a1\u4e0a\u7ebf\\\u66f4\u65b0\\\u53d8\u66f4'), (7, '\u5176\u5b83')])),
                ('description', models.TextField(verbose_name='\u4e8b\u4ef6\u63cf\u8ff0')),
                ('device_sn', models.CharField(max_length=64, verbose_name=b'AssetID', blank=True)),
                ('event_start', models.DateTimeField(verbose_name='\u4e8b\u4ef6\u5f00\u59cb\u65f6\u95f4', blank=True)),
                ('event_end', models.DateTimeField(verbose_name='\u4e8b\u4ef6\u7ed3\u675f\u65f6\u95f4', blank=True)),
                ('memo', models.TextField(verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'verbose_name': '\u53d8\u66f4\u7eaa\u5f55',
                'verbose_name_plural': '\u53d8\u66f4\u7eaa\u5f55',
            },
        ),
        migrations.CreateModel(
            name='Manufactory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64, verbose_name='\u5382\u5546\u540d\u79f0')),
                ('support_num', models.CharField(max_length=30, verbose_name='\u652f\u6301\u7535\u8bdd', blank=True)),
                ('memo', models.CharField(max_length=30, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'verbose_name': '\u5382\u5546',
                'verbose_name_plural': '\u5382\u5546',
            },
        ),
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sn', models.CharField(max_length=128, verbose_name='SN\u53f7', blank=True)),
                ('parent_sn', models.CharField(max_length=128, blank=True)),
                ('model', models.CharField(max_length=64, verbose_name='\u578b\u53f7', blank=True)),
                ('manufactory', models.CharField(max_length=32, null=True, verbose_name='\u5236\u9020\u5546', blank=True)),
                ('slot', models.CharField(max_length=32, verbose_name='\u63d2\u69fd\u4f4d', blank=True)),
                ('capacity', models.FloatField(verbose_name='\u5bb9\u91cf', blank=True)),
                ('memo', models.TextField(verbose_name='\u5907\u6ce8', blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u5185\u5b58\u90e8\u4ef6',
                'verbose_name_plural': '\u5185\u5b58\u90e8\u4ef6',
            },
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sn', models.CharField(unique=True, max_length=64, verbose_name='SN\u53f7')),
                ('manufactory', models.CharField(default=None, max_length=32, verbose_name='\u5236\u9020\u5546')),
                ('model', models.CharField(max_length=64, verbose_name='\u663e\u793a\u8bbe\u5907\u578b\u53f7')),
                ('memo', models.TextField(verbose_name='\u5907\u6ce8', blank=True)),
                ('asset', models.OneToOneField(to='api.Asset')),
            ],
            options={
                'verbose_name': '\u663e\u793a\u8bbe\u5907',
                'verbose_name_plural': '\u663e\u793a\u8bbe\u5907',
            },
        ),
        migrations.CreateModel(
            name='NetworkDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('management_ip', models.CharField(max_length=64, null=True, verbose_name='\u7ba1\u7406IP', blank=True)),
                ('vlan_ip', models.CharField(max_length=64, null=True, verbose_name='VlanIP', blank=True)),
                ('intranet_ip', models.CharField(max_length=128, null=True, verbose_name='\u5185\u7f51IP', blank=True)),
                ('sn', models.CharField(unique=True, max_length=64, verbose_name='SN\u53f7')),
                ('manufactory', models.CharField(max_length=128, null=True, verbose_name='\u5236\u9020\u5546', blank=True)),
                ('model', models.CharField(max_length=128, null=True, verbose_name='\u578b\u53f7', blank=True)),
                ('port_num', models.SmallIntegerField(null=True, verbose_name='\u7aef\u53e3\u4e2a\u6570', blank=True)),
                ('device_detail', models.TextField(null=True, verbose_name='\u8bbe\u7f6e\u8be6\u7ec6\u914d\u7f6e', blank=True)),
                ('asset', models.OneToOneField(to='api.Asset')),
            ],
            options={
                'verbose_name': '\u7f51\u7edc\u8bbe\u5907',
                'verbose_name_plural': '\u7f51\u7edc\u8bbe\u5907',
            },
        ),
        migrations.CreateModel(
            name='NIC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='\u63d2\u53e3', blank=True)),
                ('sn', models.CharField(max_length=128, verbose_name='SN\u53f7', blank=True)),
                ('parent_sn', models.CharField(max_length=128)),
                ('model', models.CharField(max_length=128, verbose_name='\u7f51\u5361\u578b\u53f7', blank=True)),
                ('manufactory', models.CharField(max_length=32, verbose_name='\u5236\u9020\u5546', blank=True)),
                ('ipaddr', models.IPAddressField(verbose_name='ip\u5730\u5740', blank=True)),
                ('mac', models.CharField(max_length=64, verbose_name='\u7f51\u5361mac\u5730\u5740')),
                ('netmask', models.CharField(max_length=64, blank=True)),
                ('memo', models.TextField(verbose_name='\u5907\u6ce8', blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u7f51\u5361\u90e8\u4ef6',
                'verbose_name_plural': '\u7f51\u5361\u90e8\u4ef6',
            },
        ),
        migrations.CreateModel(
            name='NICConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='\u63d2\u53e3', blank=True)),
                ('ipaddr', models.IPAddressField(verbose_name='ip\u5730\u5740', blank=True)),
                ('mac', models.CharField(max_length=64, verbose_name='\u7f51\u5361mac\u5730\u5740')),
                ('netmask', models.CharField(max_length=64, blank=True)),
                ('gateway', models.IPAddressField(verbose_name='\u7f51\u5173')),
                ('bonding', models.BooleanField(default=False)),
                ('memo', models.TextField(verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'verbose_name': '\u914d\u7f6e\u8868_\u7f51\u5361',
                'verbose_name_plural': '\u914d\u7f6e\u8868_\u7f51\u5361',
            },
        ),
        migrations.CreateModel(
            name='OAOrders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('oa_order_id', models.CharField(unique=True, max_length=128, verbose_name='\u5de5\u5355\u53f7')),
            ],
        ),
        migrations.CreateModel(
            name='PartitionConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('parent_sn', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=32, verbose_name='\u5206\u533a\u540d')),
                ('size', models.IntegerField(verbose_name='\u5206\u533a\u5bb9\u91cf(GB)')),
                ('fstype', models.CharField(max_length=32, verbose_name='\u6587\u4ef6\u7cfb\u7edf', choices=[(b'ntfs', b'NTFS'), (b'ext4', b'EXT4'), (b'ext3', b'EXT3'), (b'xfs', b'XFS'), (b'swap', b'SWAP')])),
                ('on_raid_group', models.CharField(default=b'group_1', max_length=128, verbose_name='\u6240\u5728Raid\u7ec4')),
            ],
        ),
        migrations.CreateModel(
            name='ProductVersion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64, verbose_name='\u4ea7\u54c1\u578b\u53f7')),
                ('version', models.CharField(max_length=64, verbose_name='\u4ea7\u54c1\u7248\u672c\u53f7', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='RaidAdaptor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sn', models.CharField(max_length=128, null=True, verbose_name='SN\u53f7', blank=True)),
                ('name', models.CharField(max_length=32, null=True, verbose_name='\u63d2\u53e3', blank=True)),
                ('parent_sn', models.CharField(max_length=128)),
                ('model', models.CharField(max_length=64, verbose_name='\u578b\u53f7', blank=True)),
                ('memo', models.TextField(verbose_name='\u5907\u6ce8', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='RaidConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('raid_group', models.CharField(max_length=128)),
                ('parent_sn', models.CharField(max_length=128)),
                ('raid_type', models.CharField(blank=True, max_length=32, null=True, verbose_name='Raid\u7c7b\u578b', choices=[(b'raid_0', b'RAID_0'), (b'raid_1', b'RAID_1'), (b'raid_5', b'RAID_5'), (b'raid_10', b'RAID_10')])),
                ('os_flag', models.BooleanField(default=False)),
                ('memo', models.TextField(verbose_name='\u5907\u6ce8', blank=True)),
                ('disks', models.ManyToManyField(to='api.Disk')),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_by', models.CharField(default=b'auto', max_length=32)),
                ('sn', models.CharField(max_length=64, verbose_name='SN\u53f7')),
                ('manufactory', models.CharField(max_length=128, null=True, verbose_name='\u5236\u9020\u5546', blank=True)),
                ('model', models.CharField(max_length=128, null=True, verbose_name='\u578b\u53f7', blank=True)),
                ('cpu_count', models.SmallIntegerField(null=True, verbose_name='cpu\u4e2a\u6570', blank=True)),
                ('cpu_core_count', models.SmallIntegerField(null=True, verbose_name='cpu\u6838\u6570', blank=True)),
                ('raid_type', models.TextField(verbose_name='raid\u7c7b\u578b', blank=True)),
                ('ram_size', models.IntegerField(verbose_name='\u5185\u5b58\u603b\u5927\u5c0fGB', blank=True)),
                ('os_type', models.CharField(max_length=64, null=True, verbose_name='\u64cd\u4f5c\u7cfb\u7edf\u7c7b\u578b', blank=True)),
                ('os_distribution', models.CharField(max_length=64, null=True, verbose_name='\u53d1\u578b\u7248\u672c', blank=True)),
                ('os_release', models.CharField(max_length=64, null=True, verbose_name='\u64cd\u4f5c\u7cfb\u7edf\u7248\u672c', blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(blank=True)),
                ('asset', models.OneToOneField(to='api.Asset')),
                ('cpu_model', models.ForeignKey(blank=True, to='api.CPU', null=True)),
                ('nic', models.ForeignKey(verbose_name='\u7f51\u5361\u5217\u8868', to='api.NIC')),
                ('physical_disk_driver', models.ForeignKey(verbose_name='\u786c\u76d8', blank=True, to='api.Disk', null=True)),
                ('raid_adaptor', models.ForeignKey(verbose_name='Raid\u5361', blank=True, to='api.RaidAdaptor', null=True)),
                ('ram', models.ForeignKey(verbose_name='\u5185\u5b58\u914d\u7f6e', blank=True, to='api.Memory', null=True)),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u5668',
                'verbose_name_plural': '\u670d\u52a1\u5668',
            },
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(default=1, help_text='eg. GNU/Linux', max_length=64, verbose_name='\u7cfb\u7edf\u7c7b\u578b', choices=[(b'linux', b'Linux'), (b'windows', b'Windows'), (b'network_firmware', b'Network Firmware'), (b'software', b'Softwares')])),
                ('distribution', models.CharField(default=b'windows', max_length=32, verbose_name='\u53d1\u578b\u7248\u672c', choices=[(b'windows', b'Windows'), (b'centos', b'CentOS'), (b'ubuntu', b'Ubuntu')])),
                ('version', models.CharField(help_text='eg. CentOS release 6.5 (Final)', unique=True, max_length=64, verbose_name='\u8f6f\u4ef6/\u7cfb\u7edf\u7248\u672c')),
                ('language', models.CharField(default=b'cn', max_length=32, verbose_name='\u7cfb\u7edf\u8bed\u8a00', choices=[(b'cn', '\u4e2d\u6587'), (b'en', '\u82f1\u6587')])),
            ],
            options={
                'verbose_name': '\u8f6f\u4ef6/\u7cfb\u7edf',
                'verbose_name_plural': '\u8f6f\u4ef6/\u7cfb\u7edf',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.SmallIntegerField(unique=True, verbose_name='\u8bbe\u5907\u72b6\u6001', choices=[(1, '\u4e0a\u67b6\uff08\u672a\u4e0a\u7ebf\uff09'), (2, '\u5e93\u5b58'), (3, '\u4e0a\u67b6\uff08\u4e0a\u7ebf\uff09'), (4, '\u4e0a\u67b6\uff08\u4e0b\u7ebf\uff09'), (5, '\u5931\u8054'), (6, '\u62a5\u5e9f'), (7, '\u786c\u4ef6\u7ef4\u62a4/\u6545\u969c')])),
                ('os_installed', models.BooleanField(default=False)),
                ('puppet_installed', models.BooleanField(default=False)),
                ('zabbix_configured', models.BooleanField(default=False)),
                ('auditing_configured', models.BooleanField(default=False)),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32, verbose_name=b'Tag name')),
            ],
        ),
        migrations.CreateModel(
            name='TaskCenter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='\u4efb\u52a1\u540d\u79f0')),
                ('description', models.TextField(null=True, verbose_name='\u63cf\u8ff0', blank=True)),
                ('task_type', models.CharField(max_length=32, verbose_name='\u4efb\u52a1\u7c7b\u578b', choices=[(b'os_installation', '\u7cfb\u7edf\u5b89\u88c5')])),
                ('content', models.TextField(default=None, verbose_name='\u4efb\u52a1\u5185\u5bb9')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('hash_str', models.CharField(max_length=64, null=True, blank=True)),
                ('memo', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('progress', models.IntegerField(default=0, verbose_name='\u8fdb\u5ea6')),
                ('result', models.CharField(max_length=32, verbose_name='\u7ed3\u679c', choices=[(b'success', '\u6210\u529f'), (b'failed', '\u5931\u8d25'), (b'processing', '\u6b63\u5728\u6267\u884c'), (b'unknown', '\u672a\u77e5')])),
                ('log', models.TextField(verbose_name='\u4efb\u52a1\u65e5\u5fd7')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='\u6700\u540e\u66f4\u65b0\u65f6\u95f4', null=True)),
                ('asset', models.ForeignKey(verbose_name='\u6267\u884c\u4efb\u52a1\u8d44\u4ea7', to='api.Asset')),
                ('task', models.ForeignKey(to='api.TaskCenter')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name='\u540d\u5b57')),
                ('token', models.CharField(max_length=128, null=True, verbose_name='token', blank=True)),
                ('department', models.CharField(max_length=32, verbose_name='\u90e8\u95e8')),
                ('email', models.EmailField(max_length=254, verbose_name='\u90ae\u7bb1')),
                ('phone', models.CharField(max_length=32, verbose_name='\u5ea7\u673a')),
                ('mobile', models.CharField(max_length=32, verbose_name='\u624b\u673a')),
                ('memo', models.TextField(verbose_name='\u5907\u6ce8', blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('backup_name', models.ForeignKey(related_name='user_backup_name', verbose_name='\u5907\u7528\u8054\u7cfb\u4eba', blank=True, to='api.UserProfile', null=True)),
                ('business_unit', models.ManyToManyField(to='api.BusinessUnit')),
                ('leader', models.ForeignKey(verbose_name=b'\xe4\xb8\x8a\xe7\xba\xa7\xe9\xa2\x86\xe5\xaf\xbc', blank=True, to='api.UserProfile', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u7528\u6237\u4fe1\u606f',
                'verbose_name_plural': '\u7528\u6237\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='WorkFlow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('workflow_type', models.CharField(max_length=64, verbose_name='\u6d41\u7a0b\u7c7b\u578b', choices=[(b'asset_offline', '\u8bbe\u5907\u4e0b\u67b6')])),
                ('application_date', models.DateTimeField(auto_now_add=True, verbose_name='\u7533\u8bf7\u65f6\u95f4')),
                ('description', models.TextField(null=True, verbose_name='\u63cf\u8ff0', blank=True)),
                ('process_time', models.DateTimeField(null=True, verbose_name='\u5904\u7406\u65f6\u95f4', blank=True)),
                ('status', models.CharField(default=b'Unhandled', max_length=32, verbose_name='\u6d41\u7a0b\u72b6\u6001')),
                ('applicant', models.ForeignKey(verbose_name='\u7533\u8bf7\u4eba', to='api.UserProfile')),
                ('asset', models.ForeignKey(verbose_name='\u6267\u884c\u8d44\u4ea7', to='api.Asset')),
                ('executor', models.ForeignKey(related_name='executor', verbose_name='\u5904\u7406\u4eba', blank=True, to='api.UserProfile', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='taskcenter',
            name='created_by',
            field=models.ForeignKey(verbose_name='\u4efb\u52a1\u521b\u5efa\u8005', blank=True, to='api.UserProfile', null=True),
        ),
        migrations.AddField(
            model_name='taskcenter',
            name='hosts',
            field=models.ManyToManyField(default=None, to='api.Configuration', verbose_name='\u9009\u62e9\u4efb\u52a1\u4e3b\u673a'),
        ),
        migrations.AlterUniqueTogether(
            name='raidadaptor',
            unique_together=set([('parent_sn', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='partitionconfig',
            unique_together=set([('parent_sn', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='nicconfig',
            unique_together=set([('name', 'mac')]),
        ),
        migrations.AlterUniqueTogether(
            name='nic',
            unique_together=set([('name', 'mac', 'parent_sn')]),
        ),
        migrations.AddField(
            model_name='networkdevice',
            name='firmware',
            field=models.ForeignKey(blank=True, to='api.Software', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='memory',
            unique_together=set([('parent_sn', 'slot')]),
        ),
        migrations.AddField(
            model_name='maintainence',
            name='applicant',
            field=models.ForeignKey(related_name='applicant_user', verbose_name='\u53d1\u8d77\u4eba', to='api.UserProfile'),
        ),
        migrations.AddField(
            model_name='maintainence',
            name='performer',
            field=models.ForeignKey(verbose_name='\u6267\u884c\u4eba', to='api.UserProfile'),
        ),
        migrations.AlterUniqueTogether(
            name='diskconfig',
            unique_together=set([('parent_sn', 'slot')]),
        ),
        migrations.AlterUniqueTogether(
            name='disk',
            unique_together=set([('parent_sn', 'slot')]),
        ),
        migrations.AddField(
            model_name='configuration',
            name='defined_partitions',
            field=models.ManyToManyField(to='api.PartitionConfig', null=True, verbose_name='\u9884\u5b9a\u4e49\u5206\u533a', blank=True),
        ),
        migrations.AddField(
            model_name='configuration',
            name='defined_raid_types',
            field=models.ManyToManyField(to='api.RaidConfig', null=True, verbose_name='\u9884\u5b9a\u4e49raid\u7c7b\u578b', blank=True),
        ),
        migrations.AddField(
            model_name='configuration',
            name='os',
            field=models.ForeignKey(verbose_name=b'OS', blank=True, to='api.Software', null=True),
        ),
        migrations.AddField(
            model_name='businessunit',
            name='contact',
            field=models.ForeignKey(default=None, to='api.UserProfile'),
        ),
        migrations.AddField(
            model_name='assetstatus',
            name='status',
            field=models.ForeignKey(default=1, verbose_name='\u8d44\u4ea7\u72b6\u6001', to='api.Status'),
        ),
        migrations.AddField(
            model_name='asset',
            name='admin',
            field=models.ForeignKey(related_name='+', verbose_name='\u8bbe\u5907\u7ba1\u7406\u5458', blank=True, to='api.UserProfile', null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='business_unit',
            field=models.ForeignKey(verbose_name='\u5c5e\u4e8e\u7684\u4e1a\u52a1\u7ebf', blank=True, to='api.BusinessUnit', null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='business_unit_level2',
            field=models.ForeignKey(verbose_name='2\u7ea7\u4e1a\u52a1\u7ebf', blank=True, to='api.BusinessUnitLevel2', null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='contract',
            field=models.ForeignKey(verbose_name='\u5408\u540c', blank=True, to='api.Contract', null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='idc',
            field=models.ForeignKey(verbose_name='IDC\u673a\u623f', blank=True, to='api.IDC', null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='tag',
            field=models.ManyToManyField(to='api.Tag', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='apiauth',
            name='users',
            field=models.ManyToManyField(to='api.UserProfile', null=True),
        ),
        migrations.AlterIndexTogether(
            name='server',
            index_together=set([('sn', 'asset')]),
        ),
        migrations.AlterUniqueTogether(
            name='raidconfig',
            unique_together=set([('parent_sn', 'raid_group')]),
        ),
        migrations.AlterUniqueTogether(
            name='apiauth',
            unique_together=set([('url', 'method_type')]),
        ),
    ]
