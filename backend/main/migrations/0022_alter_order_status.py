# Generated by Django 3.2.4 on 2021-07-11 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20210711_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('active', 'Новый'), ('finished', 'Завершена')], default='active', max_length=50),
        ),
    ]