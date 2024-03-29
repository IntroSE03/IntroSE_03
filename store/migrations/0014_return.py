# Generated by Django 3.1.7 on 2023-04-08 02:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20230407_2150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Return',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, help_text='This is the quantity of this partiuclar book purchased')),
                ('price', models.FloatField(help_text='This is the price of one of this product')),
                ('address', models.CharField(blank=True, default='', help_text='This is the customer address', max_length=50)),
                ('phone', models.CharField(blank=True, default='', help_text='This is the customer phone number', max_length=50)),
                ('date', models.DateField(default=datetime.datetime.today, help_text='This is the date the order was placed')),
                ('status', models.BooleanField(default=False, help_text='Check this box to mark the order complete')),
                ('customer', models.ForeignKey(help_text='This is the customer purchasing the book', on_delete=django.db.models.deletion.CASCADE, to='store.customer')),
                ('product', models.ForeignKey(help_text='This is the book title', on_delete=django.db.models.deletion.CASCADE, to='store.products')),
            ],
        ),
    ]
