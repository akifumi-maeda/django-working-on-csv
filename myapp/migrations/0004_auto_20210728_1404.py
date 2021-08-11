# Generated by Django 3.2.5 on 2021-07-28 05:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20210728_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 28, 5, 4, 43, 368452, tzinfo=utc), verbose_name='受注日'),
        ),
        migrations.AlterField(
            model_name='order',
            name='section',
            field=models.CharField(blank=True, choices=[('', '---------'), ('1F', '1F'), ('1FA', '1FA'), ('1J', '1J'), ('1JA', '1JA'), ('1P', '1P'), ('1PA', '1PA'), ('1S', '1S'), ('2F', '2F'), ('2FA', '2FA'), ('2J', '2J'), ('2JA', '2JA'), ('2P', '2P'), ('2PA', '2PA')], default='', max_length=3, null=True, verbose_name='摘要'),
        ),
        migrations.AlterField(
            model_name='orderwork',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 28, 5, 4, 43, 369066, tzinfo=utc), verbose_name='日付'),
        ),
    ]
