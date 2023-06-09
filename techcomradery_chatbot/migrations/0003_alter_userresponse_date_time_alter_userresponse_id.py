# Generated by Django 4.1.7 on 2023-03-16 18:15

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('techcomradery_chatbot', '0002_alter_userresponse_date_time_alter_userresponse_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userresponse',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 16, 23, 45, 41, 137910, tzinfo=datetime.timezone.utc), editable=False, verbose_name='Response Time'),
        ),
        migrations.AlterField(
            model_name='userresponse',
            name='id',
            field=models.UUIDField(default=uuid.UUID('c661e5c9-205c-4ce6-b9ed-1b82d124a21e'), editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Response ID'),
        ),
    ]
