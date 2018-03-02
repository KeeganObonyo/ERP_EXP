# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime
import django.utils.timezone
import django.core.validators
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, error_messages={'unique': 'A user with that username already exists.'}, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], max_length=30, verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(help_text='Designates whether the user can log into this admin site.', default=False, verbose_name='staff status')),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('additional_info', models.CharField(blank=True, null=True, max_length=100)),
                ('groups', models.ManyToManyField(to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', blank=True, verbose_name='groups')),
                ('provider', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='provider_rel_+')),
                ('user_permissions', models.ManyToManyField(to='auth.Permission', help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', blank=True, verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'users',
                'abstract': False,
                'verbose_name': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('street', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('zip_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('main_id_type_no', models.CharField(blank=True, null=True, max_length=50)),
                ('birthday', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('siblings', models.CharField(blank=True, null=True, max_length=20)),
                ('no_in_household', models.CharField(blank=True, null=True, max_length=20)),
                ('religion', models.CharField(blank=True, null=True, max_length=50)),
                ('preferred_language', models.CharField(blank=True, null=True, max_length=20)),
                ('phone_number', models.CharField(blank=True, null=True, max_length=50)),
                ('notes', models.CharField(db_index=True, blank=True, max_length=200)),
                ('address', models.ForeignKey(to='accounts.Address', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BloodType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('first_name', models.CharField(db_index=True, blank=True, max_length=200)),
                ('last_name', models.CharField(db_index=True, blank=True, max_length=200)),
                ('phone_number', models.CharField(db_index=True, blank=True, max_length=200)),
                ('email', models.CharField(db_index=True, blank=True, max_length=200)),
                ('location', models.CharField(db_index=True, blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('description', models.CharField(db_index=True, blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ethnicity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='IdentificationType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MaritalStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(db_index=True, blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('phone', models.IntegerField(db_index=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(db_index=True, blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sex',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(db_index=True, blank=True, max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='bio',
            name='blood_type',
            field=models.ForeignKey(to='accounts.BloodType', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bio',
            name='em_c_relationship',
            field=models.ForeignKey(to='accounts.Relationship', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bio',
            name='em_contact',
            field=models.ForeignKey(to='accounts.EmergencyContact', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bio',
            name='employment',
            field=models.ForeignKey(to='accounts.Employment', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bio',
            name='ethnicity',
            field=models.ForeignKey(to='accounts.Ethnicity', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bio',
            name='gender',
            field=models.ManyToManyField(to='accounts.Sex'),
        ),
        migrations.AddField(
            model_name='bio',
            name='id_type',
            field=models.ForeignKey(to='accounts.IdentificationType', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bio',
            name='marital_status',
            field=models.ForeignKey(to='accounts.MaritalStatus', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bio',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, blank=True, null=True),
        ),
    ]
