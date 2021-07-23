# Generated by Django 3.2.4 on 2021-07-23 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_merge_20210721_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='document',
            name='type_doc',
            field=models.CharField(choices=[('other', 'Прочее'), ('specification', 'Спецификация'), ('contract_for_signing', 'Договор на подписание'), ('payment_invoice', 'Счет на оплату'), ('quality_certificate', 'Сертификат качества'), ('contract', 'Договор'), ('payment_order', 'Платежное поручение'), ('verification_act', 'Акт сверки'), ('book_of_purchases_or_sales', 'Книга покупок/продаж'), ('letter_for_refund', 'Письмо на возврат'), ('loading_plan', 'План погрузки'), ('report_on_the_shipped_goods', 'Отчет о погруженном товаре'), ('additional_payment_invoice', 'Счет на доплату')], default='other', max_length=250, verbose_name='Тип документа'),
        ),
        migrations.AddField(
            model_name='culture',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.category'),
            preserve_default=False,
        ),
    ]
