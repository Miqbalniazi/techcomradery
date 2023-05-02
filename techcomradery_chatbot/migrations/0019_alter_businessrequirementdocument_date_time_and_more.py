# Generated by Django 4.1.1 on 2023-04-29 07:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techcomradery_chatbot', '0018_alter_businessrequirementdocument_date_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessrequirementdocument',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 29, 12, 48, 33, 527691, tzinfo=datetime.timezone.utc), editable=False, verbose_name='Created Date Time'),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 29, 12, 48, 33, 512068, tzinfo=datetime.timezone.utc), editable=False, verbose_name='Created Date Time'),
        ),
        migrations.AlterField(
            model_name='userresponse',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 29, 12, 48, 33, 527691, tzinfo=datetime.timezone.utc), editable=False, verbose_name='Response Time'),
        ),
    ]
