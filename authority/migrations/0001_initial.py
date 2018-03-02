# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('codename', models.CharField(max_length=100, verbose_name='codename')),
                ('object_id', models.PositiveIntegerField()),
                ('approved', models.BooleanField(help_text='Designates whether the permission has been approved and treated as active. Unselect this instead of deleting permissions.', default=False, verbose_name='approved')),
                ('date_requested', models.DateTimeField(default=datetime.datetime.now, verbose_name='date requested')),
                ('date_approved', models.DateTimeField(blank=True, null=True, verbose_name='date approved')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', related_name='row_permissions')),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='created_permissions', blank=True, null=True)),
                ('group', models.ForeignKey(to='auth.Group', blank=True, null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='granted_permissions', blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'permissions',
                'permissions': (('change_foreign_permissions', 'Can change foreign permissions'), ('delete_foreign_permissions', 'Can delete foreign permissions'), ('approve_permission_requests', 'Can approve permission requests')),
                'verbose_name': 'permission',
            },
        ),
        migrations.AlterUniqueTogether(
            name='permission',
            unique_together=set([('codename', 'object_id', 'content_type', 'user', 'group')]),
        ),
    ]
