from django.db import models

# Create your models here.

from django.utils import timezone
from django.urls import reverse

class Order(models.Model):
    CHOICES = [
        (None, '---------'),
        ('1F', '1F'),
        ('1FA', '1FA'),
        ('1J', '1J'),
        ('1JA', '1JA'),
        ('1P', '1P'),
        ('1PA', '1PA'),
        ('1S', '1S'),
        ('2F', '2F'),
        ('2FA', '2FA'),
        ('2J', '2J'),
        ('2JA', '2JA'),
        ('2P', '2P'),
        ('2PA', '2PA'),
    ]

    order_number = models.CharField(max_length=15, primary_key=True, verbose_name='依頼No.')
    order_date = models.DateField(verbose_name='受注日', default=timezone.now())
    management_number = models.CharField(max_length=10, verbose_name='管理番号')
    management_code = models.CharField(max_length=10, verbose_name='管理コード')
    name = models.CharField(max_length=100, verbose_name='品名')
    lot_number = models.CharField(max_length=20, verbose_name='Lot No.')
    work_content = models.CharField(max_length=50, verbose_name='作業内容')
    unit_price = models.FloatField(verbose_name='単価')
    number = models.PositiveIntegerField(verbose_name='受注数')
    section = models.CharField(max_length=3, choices=CHOICES, blank=True, null=True, default=None, verbose_name='摘要')

    class Meta:
        ordering = ['order_date', 'order_number', 'management_number', 'management_code', 'section']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("order_detail", kwargs={"pk": self.order_number})


class Worker(models.Model):
    id = models.CharField(max_length=6, primary_key=True, verbose_name='作業者コード')
    name = models.CharField(max_length=20, verbose_name='作業者名')

    def __str__(self):
        return self.name

class OrderWork(models.Model):
    date = models.DateField(default=timezone.now(), verbose_name='日付')
    worker = models.ForeignKey('Worker', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='作業者名')
    order = models.ForeignKey('Order', on_delete=models.RESTRICT, verbose_name='オーダー')
    number = models.PositiveIntegerField(verbose_name='作業数量')
    start_time = models.TimeField(verbose_name='開始時刻')
    finish_time = models.TimeField(verbose_name='終了時刻')