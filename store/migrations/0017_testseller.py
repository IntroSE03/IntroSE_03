# Generated by Django 4.1.7 on 2023-05-03 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_auto_20230501_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='testSeller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Enter first name, max 50 characters', max_length=50)),
                ('last_name', models.CharField(help_text='Enter last name, max 50 characters', max_length=50)),
                ('email', models.EmailField(help_text='Enter email in name@provider.com format', max_length=254)),
                ('username', models.CharField(help_text='Enter Username, max 50 characters', max_length=50)),
            ],
        ),
    ]
