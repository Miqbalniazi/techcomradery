# Generated by Django 4.1.7 on 2023-03-29 20:35

from django.db import migrations, models
import techcomradery_client.models


class Migration(migrations.Migration):

    dependencies = [
        ('techcomradery_client', '0003_subscriptionuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionuser',
            name='referral',
            field=models.CharField(default=techcomradery_client.models.get_referral, editable=False, max_length=10, verbose_name='Referral ID'),
        ),
    ]
