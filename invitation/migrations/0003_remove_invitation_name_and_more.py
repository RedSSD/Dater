# Generated by Django 5.0 on 2024-01-01 11:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0002_alter_invitation_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitation',
            name='name',
        ),
        migrations.AlterField(
            model_name='invitation',
            name='expiration_date',
            field=models.DateField(default=datetime.date(2024, 1, 3)),
        ),
    ]
