# Generated by Django 5.1.3 on 2025-01-01 14:22

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internal_id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Internal ID', unique=True, verbose_name='Internal ID')),
                ('is_active', models.BooleanField(default=True, help_text='Indicates whether the object is active or not', verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The date and time when the object was created', null=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='The date and time when the object was last updated', null=True, verbose_name='Updated At')),
                ('payment_method', models.CharField(choices=[('CASH', 'Cash'), ('CARD', 'Card'), ('UPI', 'UPI')], max_length=255, verbose_name='Payment Method')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount')),
                ('status', models.CharField(choices=[('paid', 'Paid'), ('partially_paid', 'Partially Paid'), ('failed', 'Failed'), ('refunded', 'Refunded'), ('pending', 'Pending'), ('cancelled', 'Cancelled')], default='pending', max_length=255, verbose_name='Payment Status')),
                ('payment_date', models.DateTimeField(verbose_name='Payment Date')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='orders.order')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
                'db_table': 'payments',
            },
        ),
    ]
