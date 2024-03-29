# Generated by Django 3.2.4 on 2021-07-25 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_rename_customer_cost_order_farmer_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='company_name',
        ),
        migrations.AddField(
            model_name='company',
            name='mail_address',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Почтовый адрес'),
        ),
        migrations.AddField(
            model_name='order',
            name='company',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='main.company'),
            preserve_default=False,
        ),
    ]
