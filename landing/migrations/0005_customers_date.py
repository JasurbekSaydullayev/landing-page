# Generated by Django 5.1.4 on 2024-12-22 16:41

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_customers_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]