# Generated by Django 4.1.7 on 2023-03-16 12:15

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('techcomradery_chatbot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userresponse',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 16, 17, 45, 2, 873498), editable=False, verbose_name='Response Time'),
        ),
        migrations.AlterField(
            model_name='userresponse',
            name='id',
            field=models.UUIDField(default=uuid.UUID('3a183667-327b-4f95-bfc9-4c2fed525f8e'), editable=False, primary_key=True, serialize=False, verbose_name='Response ID'),
        ),
    ]
