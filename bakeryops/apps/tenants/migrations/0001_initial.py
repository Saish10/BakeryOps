# Generated by Django 5.1.3 on 2024-12-25 06:53

import django.db.models.deletion
import django_tenants.postgresql_backend.base
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schema_name', models.CharField(db_index=True, max_length=63, unique=True, validators=[django_tenants.postgresql_backend.base._check_schema_name])),
                ('name', models.CharField(help_text='Enter a Tenant name', max_length=255, verbose_name='Tenant Name')),
                ('email', models.EmailField(db_index=True, help_text='Enter a valid email address (e.g., example@domain.com).', max_length=254, unique=True, verbose_name='Email Address')),
            ],
            options={
                'verbose_name': 'Tenant',
                'verbose_name_plural': 'Tenants',
                'db_table': 'tenant',
            },
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(db_index=True, max_length=253, unique=True)),
                ('is_primary', models.BooleanField(db_index=True, default=True)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domains', to='tenants.tenant')),
            ],
            options={
                'verbose_name': 'Tenant Domain',
                'verbose_name_plural': 'Tenant Domains',
                'db_table': 'domain',
            },
        ),
    ]