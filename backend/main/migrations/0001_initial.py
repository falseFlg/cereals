# Generated by Django 3.2.4 on 2021-07-14 07:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CarsForShipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('deliver', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_provider', models.CharField(max_length=250, verbose_name='Название компании')),
                ('head_of_provider', models.CharField(blank=True, default='', max_length=250, verbose_name='ФИО руководителя компании')),
                ('short_fio', models.CharField(blank=True, default='', max_length=250, verbose_name='сокращенное ФИО руководителя компании')),
                ('position_head_of_provider', models.CharField(blank=True, default='', max_length=250, verbose_name='Должность руководителя компании')),
                ('basis_of_doc', models.CharField(blank=True, default='', max_length=250, verbose_name='Должность руководителя компании')),
                ('address_load', models.CharField(blank=True, default='', max_length=250, verbose_name='Должность руководителя компании')),
                ('ul_address', models.CharField(blank=True, default='', max_length=500, verbose_name='Юридический адрес компании')),
                ('inn', models.CharField(blank=True, default='', max_length=500, verbose_name='ИНН компании')),
                ('kpp', models.CharField(blank=True, default='', max_length=500, verbose_name='КПП компании')),
                ('ogrn', models.CharField(blank=True, default='', max_length=500, verbose_name='ОГРН компании')),
                ('bik', models.CharField(blank=True, default='', max_length=250, verbose_name='БИК компании')),
                ('payment_account', models.CharField(blank=True, default='', max_length=250, verbose_name='Расчетный счет компании')),
                ('correspondent_account', models.CharField(blank=True, default='', max_length=250, verbose_name='Корреспондентский счет компании')),
                ('phone_number', models.CharField(blank=True, default='', max_length=64, verbose_name='Телефонный номер компании')),
                ('email_of_head', models.CharField(blank=True, default='', max_length=250, verbose_name='Email руководителя')),
                ('name_of_bank', models.CharField(blank=True, default='', max_length=250, verbose_name='Название банка')),
            ],
        ),
        migrations.CreateModel(
            name='Culture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=250, verbose_name='Имя документа')),
                ('type_doc', models.CharField(blank=True, max_length=250, null=True, verbose_name='Тип документа')),
                ('file', models.FileField(null=True, upload_to='uploads/%Y/%m/%d/%H/%M/%S', verbose_name='Файл')),
                ('sign_file', models.FileField(null=True, upload_to='uploads/%Y/%m/%d/%H/%M/%S', verbose_name='Файл подписи')),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок')),
                ('volume', models.IntegerField(verbose_name='Объем')),
                ('description', models.TextField(blank=True, default='', verbose_name='Описание')),
                ('status', models.CharField(choices=[('active', 'Активный'), ('archived', 'Архивирован'), ('accepted', 'Принят'), ('pending', 'В процессе'), ('partial', 'Частично выполнен')], default='active', max_length=250, verbose_name='Статус')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано (время)')),
                ('date_start_shipment', models.DateTimeField(blank=True, null=True, verbose_name='Дата старта поставки')),
                ('date_finish_shipment', models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания поставки')),
                ('cost', models.IntegerField()),
                ('tax_type', models.CharField(choices=[('simple', 'Упрощенная')], default='simple', max_length=25)),
                ('company_name', models.CharField(blank=True, default='', max_length=225)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UnitOfMeasurementOfSpecification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=250, verbose_name='Единица измерения')),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=250, verbose_name='Название')),
                ('address', models.CharField(max_length=250, null=True, verbose_name='Адрес')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WarehouseDistance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.IntegerField()),
                ('price', models.IntegerField()),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='starts', to='main.warehouse')),
                ('to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ends', to='main.warehouse')),
            ],
        ),
        migrations.CreateModel(
            name='SpecificationsOfProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('required', models.BooleanField(default=False)),
                ('type', models.CharField(choices=[('int', 'Целочисленное'), ('range', 'Диапозон'), ('string', 'Строковое'), ('bool', 'Логическое'), ('decimal', 'Десятичное')], max_length=255)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('GOST', models.CharField(blank=True, max_length=250, null=True, verbose_name='ГОСТ')),
                ('default', models.TextField(blank=True, null=True)),
                ('unit_of_measurement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unit_of_measurement', to='main.unitofmeasurementofspecification')),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=250)),
                ('cars', models.ManyToManyField(to='main.CarsForShipment')),
                ('documents', models.ManyToManyField(to='main.Document')),
            ],
        ),
        migrations.CreateModel(
            name='RateForDelivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_per_tonne', models.IntegerField(blank=True, null=True, verbose_name='Стоимость за 1 тонну')),
                ('min', models.IntegerField(blank=True, null=True)),
                ('max', models.IntegerField(blank=True, null=True)),
                ('delta', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('way', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates', to='main.warehousedistance')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('admin', 'Админ'), ('customer', 'Фермер'), ('crm', 'Провайдер')], default='customer', max_length=25)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='main.company')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, null=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('harvest_year', models.DateField(blank=True, null=True, verbose_name='Год урожая')),
                ('harvest_type', models.CharField(blank=True, max_length=250, null=True, verbose_name='Тип урожая')),
                ('culture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.culture')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('active', 'Новый'), ('finished', 'Завершена'), ('failed', 'Проваленная сделка')], default='active', max_length=50)),
                ('accepted_volume', models.IntegerField()),
                ('name_of_contract', models.CharField(blank=True, default='', max_length=250, verbose_name='Название договора')),
                ('number_of_spec', models.CharField(blank=True, default='', max_length=250, verbose_name='Номер спецификации')),
                ('date_start_of_spec', models.DateTimeField(blank=True, null=True, verbose_name='Дата начала спецификации')),
                ('date_finish_of_spec', models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания спецификации')),
                ('date_start_of_contract', models.DateTimeField(blank=True, null=True, verbose_name='Дата начала договора')),
                ('date_finish_of_contract', models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания договора')),
                ('date_start_shipment', models.DateTimeField(blank=True, null=True, verbose_name='Дата старта экспорта')),
                ('date_finish_shipment', models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания экспорта')),
                ('amount_of_NDS', models.IntegerField(default=0, verbose_name='Размер НДС')),
                ('customer_cost', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL)),
                ('documents', models.ManyToManyField(blank=True, to='main.Document')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='main.offer')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provider', to=settings.AUTH_USER_MODEL)),
                ('selected_warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.warehouse')),
            ],
        ),
        migrations.CreateModel(
            name='OfferSpecification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField(blank=True, null=True)),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specification_values', to='main.offer')),
                ('specification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specification_values', to='main.specificationsofproduct')),
            ],
        ),
        migrations.AddField(
            model_name='offer',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product'),
        ),
        migrations.AddField(
            model_name='offer',
            name='specifications',
            field=models.ManyToManyField(blank=True, related_name='specifications', through='main.OfferSpecification', to='main.SpecificationsOfProduct'),
        ),
        migrations.AddField(
            model_name='offer',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.warehouse'),
        ),
        migrations.AddField(
            model_name='culture',
            name='specifications',
            field=models.ManyToManyField(blank=True, related_name='categories', to='main.SpecificationsOfProduct'),
        ),
    ]
