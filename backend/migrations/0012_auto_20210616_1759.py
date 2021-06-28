# Generated by Django 3.2.3 on 2021-06-16 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='correspondent_account',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Корреспондентский счет компании'),
        ),
        migrations.AlterField(
            model_name='company',
            name='payment_account',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Расчетный счет компании'),
        ),
    ]
