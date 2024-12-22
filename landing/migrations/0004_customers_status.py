# Generated by Django 5.1.4 on 2024-12-22 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_remove_customers_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='New', max_length=100),
        ),
    ]