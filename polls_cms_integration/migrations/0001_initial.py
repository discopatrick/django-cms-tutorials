# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-29 15:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PollPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='polls_cms_integration_pollpluginmodel', serialize=False, to='cms.CMSPlugin')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Poll')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
