# Generated by Django 3.2.3 on 2021-06-16 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_auto_20210616_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='bik',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='БИК компании'),
        ),
    ]
