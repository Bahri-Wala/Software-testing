# Generated by Django 3.2.6 on 2021-08-20 13:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0026_auto_20210820_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(default=datetime.date(2021, 8, 10)),
        ),
    ]
