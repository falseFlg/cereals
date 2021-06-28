# Generated by Django 3.2.3 on 2021-06-10 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210604_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='file',
            field=models.FileField(null=True, upload_to='uploads/%Y/%m/%d/', verbose_name='Файл'),
        ),
        migrations.AddField(
            model_name='document',
            name='name',
            field=models.CharField(default='', max_length=250, verbose_name='Имя документа'),
        ),
        migrations.AddField(
            model_name='document',
            name='type_doc',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Тип документа'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Создано (время)'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='offer_lifetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время жизни предложения'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='period_of_export',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Период экспорта'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='status',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='volume',
            field=models.IntegerField(blank=True, null=True, verbose_name='Объем'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='harvest_type',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Тип урожая'),
        ),
        migrations.AlterField(
            model_name='product',
            name='moisture',
            field=models.IntegerField(blank=True, null=True, verbose_name='Влажность'),
        ),
        migrations.AlterField(
            model_name='product',
            name='vitreous',
            field=models.IntegerField(blank=True, null=True, verbose_name='Стекловидность'),
        ),
    ]