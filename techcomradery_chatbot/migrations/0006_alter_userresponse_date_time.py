# Generated by Django 4.1.7 on 2023-03-24 20:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techcomradery_chatbot', '0005_userresponse_brd_id_alter_userresponse_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userresponse',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 25, 2, 12, 19, 543487, tzinfo=datetime.timezone.utc), editable=False, verbose_name='Response Time'),
        ),
    ]