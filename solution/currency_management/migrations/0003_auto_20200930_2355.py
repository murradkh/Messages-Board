# Generated by Django 3.1.1 on 2020-09-30 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency_management', '0002_auto_20200930_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='currency_name',
            field=models.CharField(choices=[('USD', 'United States Dollar'), ('CAD', 'Canadian Dollar'), ('JPY', 'Japaneses Yen'), ('GBP', 'Great Briton Pound'), ('EUR', 'Euro')], max_length=3),
        ),
    ]
