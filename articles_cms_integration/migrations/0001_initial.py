# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-12 00:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlePluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='articles_cms_integration_articlepluginmodel', serialize=False, to='cms.CMSPlugin')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
