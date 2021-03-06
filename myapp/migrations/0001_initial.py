# Generated by Django 3.2.5 on 2021-07-28 03:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_number', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='依頼No.')),
                ('order_date', models.DateField(default=datetime.date(2021, 7, 28), verbose_name='受注日')),
                ('management_number', models.CharField(max_length=10, verbose_name='管理番号')),
                ('management_code', models.CharField(max_length=10, verbose_name='管理コード')),
                ('name', models.CharField(max_length=50, verbose_name='品名')),
                ('lot_number', models.CharField(max_length=12, verbose_name='Lot No.')),
                ('work_content', models.CharField(max_length=20, verbose_name='作業内容')),
                ('unit_price', models.FloatField(verbose_name='単価')),
                ('number', models.PositiveIntegerField(verbose_name='受注数')),
                ('section', models.CharField(choices=[('', '---------'), ('1F', '1F'), ('1FA', '1FA'), ('1J', '1J'), ('1JA', '1JA'), ('1P', '1P'), ('1PA', '1PA'), ('1S', '1S'), ('2F', '2F'), ('2FA', '2FA'), ('2J', '2J'), ('2JA', '2JA'), ('2P', '2P'), ('2PA', '2PA')], default='', max_length=3, verbose_name='摘要')),
            ],
            options={
                'ordering': ['order_date', 'order_number', 'management_number', 'management_code', 'section'],
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='作業者コード')),
                ('name', models.CharField(max_length=20, verbose_name='作業者名')),
            ],
        ),
        migrations.CreateModel(
            name='OrderWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date(2021, 7, 28), verbose_name='日付')),
                ('number', models.PositiveIntegerField(verbose_name='作業数量')),
                ('start_time', models.TimeField(verbose_name='開始時刻')),
                ('finish_time', models.TimeField(verbose_name='終了時刻')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='myapp.order', verbose_name='オーダー')),
                ('worker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.worker', verbose_name='作業者名')),
            ],
        ),
    ]
