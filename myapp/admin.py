from django.contrib import admin
from django.db import models
from .models import Order, Worker, OrderWork

# Register your models here.

class OrderWorksInline(admin.TabularInline):
    model = OrderWork

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_filter = ('section',)
    inlines = [OrderWorksInline]

admin.site.register(Worker)
admin.site.register(OrderWork)