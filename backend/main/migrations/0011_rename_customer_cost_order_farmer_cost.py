# Generated by Django 3.2.4 on 2021-07-23 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_offer_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer_cost',
            new_name='farmer_cost',
        ),
    ]
