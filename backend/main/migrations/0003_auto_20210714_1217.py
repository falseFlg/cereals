# Generated by Django 3.2.4 on 2021-07-14 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210714_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='date_finish_shipment',
            field=models.DateField(blank=True, null=True, verbose_name='Дата окончания поставки'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='date_start_shipment',
            field=models.DateField(blank=True, null=True, verbose_name='Дата старта поставки'),
        ),
    ]
