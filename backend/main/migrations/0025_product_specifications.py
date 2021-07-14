# Generated by Django 3.2.4 on 2021-07-13 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20210713_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='specifications',
            field=models.ManyToManyField(blank=True, related_name='specifications', through='main.ProductSpecification', to='main.SpecificationsOfProduct'),
        ),
    ]