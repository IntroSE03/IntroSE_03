# Generated by Django 3.1.7 on 2023-05-01 20:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_remove_return_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Enter first name, max 50 characters', max_length=50)),
                ('last_name', models.CharField(help_text='Enter last name, max 50 characters', max_length=50)),
                ('email', models.EmailField(help_text='Enter email in name@provider.com format', max_length=254)),
                ('username', models.CharField(help_text='Enter Username, max 50 characters', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='return',
            name='customer',
            field=models.ForeignKey(help_text='This is the customer returning the book', on_delete=django.db.models.deletion.CASCADE, to='store.customer'),
        ),
        migrations.AlterField(
            model_name='return',
            name='date',
            field=models.DateField(default=datetime.datetime.today, help_text='This is the date the return was placed'),
        ),
        migrations.AlterField(
            model_name='return',
            name='quantity',
            field=models.IntegerField(default=1, help_text='This is the quantity of this partiuclar book being returned'),
        ),
        migrations.AlterField(
            model_name='return',
            name='status',
            field=models.BooleanField(default=False, help_text='Check this box to mark the return complete'),
        ),
    ]
