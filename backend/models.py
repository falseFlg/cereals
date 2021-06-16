from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField('Название', max_length=250)
    description = models.TextField('Описание', blank=True, null=True)
    amount_of_gluten = models.IntegerField('Количество клейковины', blank=True, null=True)
    vitreous = models.IntegerField('Стекловидность', blank=True, null=True)
    nature = models.IntegerField('Натура', blank=True, null=True)
    moisture = models.IntegerField('Влажность', blank=True, null=True)
    weed_admixture = models.IntegerField('Сорная примесь', blank=True, null=True)
    harvest_year = models.DateField('Год урожая', blank=True, null=True)
    harvest_type = models.CharField('Тип урожая', max_length=250, blank=True, null=True)
    humidity = models.IntegerField('Влажность', blank=True, null=True)
    grain_impurity = models.IntegerField('Зерновая примесь', blank=True, null=True)
    broken = models.IntegerField('Битые', blank=True, null=True)
    damaged_by_mold = models.IntegerField('Поврежденные плесенью', blank=True, null=True)
    aflatoxin = models.IntegerField('Афлатоксин', blank=True, null=True)
    vomitoxin = models.IntegerField('Вомитоксин', blank=True, null=True)
    protein = models.IntegerField('Протеин', blank=True, null=True)
    drop_number = models.IntegerField('Число падения', blank=True, null=True)
    damage_bedbug_turtle = models.IntegerField('Повреждение клопом черепашкой', blank=True, null=True)
    alveographic_characteristics_of_the_test = models.IntegerField(
        'Альвеографические характеристики теста', blank=True, null=True)
    gluten_strain_gauge = models.IntegerField('Измеритель деформации клейковины', blank=True, null=True)
    damaged = models.IntegerField('Поврежденные', blank=True, null=True)
    colored = models.IntegerField('Цветные', blank=True, null=True)
    oilseed_admixture = models.IntegerField('Масличная примесь', blank=True, null=True)
    oil_content = models.IntegerField('Масличность', blank=True, null=True)
    acid_number_of_the_oil = models.IntegerField('Кислотное число масла', blank=True, null=True)
    free_fatty_acids = models.IntegerField('Свободные жирные кислоты', blank=True, null=True)
    salmonella = models.IntegerField('Сальмонелла', blank=True, null=True)
    pesticides = models.IntegerField('Пестициды', blank=True, null=True)
    erucic_acid = models.IntegerField('Эруковая кислота', blank=True, null=True)
    glucosinolates = models.IntegerField('Глюкозинолаты', blank=True, null=True)
    genetically_modified_organism = models.IntegerField('Генетически модифицированный организм', blank=True, null=True)
    fiber = models.IntegerField('Клетчатка', blank=True, null=True)
    dirty_chickpeas = models.IntegerField('Грязный нут', blank=True, null=True)
    passing_through_the_sieve = models.IntegerField('Проход через сито', blank=True, null=True)
    smell = models.IntegerField('Запах', blank=True, null=True)
    harmful_substances = models.IntegerField('Вредные вещества', blank=True, null=True)
    urea = models.IntegerField('Мочевина', blank=True, null=True)
    potassium_hydroxide = models.IntegerField('Гидрооксид калия', blank=True, null=True)
    trypsin = models.IntegerField('Трипсин', blank=True, null=True)
    ochratoxin = models.IntegerField('Охратоксин', blank=True, null=True)
    zearalenon = models.IntegerField('Зеараленон', blank=True, null=True)
    fumonisin = models.IntegerField('Фумонизин', blank=True, null=True)
    damaged_by_drying = models.IntegerField('Поврежденные сушкой', blank=True, null=True)
    damaged_by_pests = models.IntegerField('Поврежденные вредителями', blank=True, null=True)
    other_cereals = models.IntegerField('Прочие зерновые', blank=True, null=True)
    infection_is_not_allowed = models.BooleanField('Зараженность не допускается', blank=True, null=True)

    def __str__(self):
        return self.title


class Warehouse(models.Model):
    title = models.CharField('Название', max_length=250, default='')
    address = models.CharField('Адрес', max_length=250)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')  # TODO

    def __str__(self):
        return self.title


class Offer(models.Model):
    title = models.CharField('Заголовок', max_length=250)
    volume = models.IntegerField('Объем', blank=True, null=True)
    description = models.TextField('Описание', blank=True, null=True)
    offer_lifetime = models.DateTimeField('Время жизни предложения', blank=True, null=True)
    status = models.CharField('Статус', max_length=250, blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Создатель', blank=True, null=True)  # TODO
    created_at = models.DateTimeField('Создано (время)', auto_now_add=True)
    product = models.ForeignKey(Product, related_name='Культура', on_delete=models.CASCADE, blank=True, null=True)
    warehouses = models.ManyToManyField(Warehouse, blank=True)
    period_of_export = models.DateTimeField('Период экспорта', blank=True, null=True)

    @property
    def cost_by_tonne(self):
        return 0

    def __str__(self):
        return self.title



class Notification(models.Model):
    pass


class Document(models.Model):
    name = models.CharField('Имя документа', max_length=250, default='')
    type_doc = models.CharField('Тип документа', max_length=250, null=True, blank=True)
    file = models.FileField('Файл', upload_to='uploads/%Y/%m/%d/%H/%M/%S', null=True)
    sign_file = models.FileField('Файл подписи', upload_to='uploads/%Y/%m/%d/%H/%M/%S', null=True)


class QualityControl(models.Model):
    pass

class Payment(models.Model):
    pass


class CarsForShipment(models.Model):
    name = models.CharField(max_length=250)
    company = models.CharField(max_length=250)
    shipment_fact = models.IntegerField()

    pass



class Shipment(models.Model):
    status = models.CharField(max_length=250)
    documents = models.ManyToManyField(Document)
    cars = models.ManyToManyField(CarsForShipment)
    pass

class Сontrol(models.Model):
    pass


class Deal(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='offer')
    status = models.CharField(max_length=250)
    provider = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Поставщик', blank=True, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Покупатель', blank=True, null=True)
    documents = models.ManyToManyField(Document)
    quality_control = models.ManyToManyField(QualityControl)
    payment = models.ManyToManyField(Payment)
    shipment = models.ManyToManyField(Shipment)
    control = models.ManyToManyField(Сontrol)


    pass

