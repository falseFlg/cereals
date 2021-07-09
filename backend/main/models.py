from datetime import datetime, timezone
from decimal import Decimal
from typing import Optional

from django.contrib.auth.models import User
from django.db import models

from main.consts import NDS
from main.enums import SpecificationTypes, OfferStatus, OrderStatus
from main.managers.offer import OfferManager
from main.querysets.offer import OfferQuerySet, DeliveryPrice


# Для Sign
class Company(models.Model):
    name_of_provider = models.CharField("Название компании", max_length=250)
    head_of_provider = models.CharField(
        "ФИО руководителя компании", max_length=250, blank=True, default=""
    )
    short_fio = models.CharField(
        "сокращенное ФИО руководителя компании", max_length=250, blank=True, default=""
    )
    position_head_of_provider = models.CharField(
        "Должность руководителя компании", max_length=250, blank=True, default=""
    )
    basis_of_doc = models.CharField(
        "Должность руководителя компании", max_length=250, blank=True, default=""
    )
    address_load = models.CharField(
        "Должность руководителя компании", max_length=250, blank=True, default=""
    )
    ul_address = models.CharField(
        "Юридический адрес компании", max_length=500, blank=True, default=""
    )
    inn = models.CharField("ИНН компании", blank=True, default="", max_length=500)
    kpp = models.CharField("КПП компании", blank=True, default="", max_length=500)
    ogrn = models.CharField("ОГРН компании", blank=True, default="", max_length=500)
    bik = models.CharField("БИК компании", max_length=250, blank=True, default="")
    payment_account = models.CharField(
        "Расчетный счет компании", max_length=250, blank=True, default="",
    )
    correspondent_account = models.CharField(
        "Корреспондентский счет компании", max_length=250, blank=True, default="",
    )
    phone_number = models.CharField(
        "Телефонный номер компании", max_length=64, blank=True, default="",
    )
    email_of_head = models.CharField(
        "Email руководителя", max_length=250, blank=True, default="",
    )
    name_of_bank = models.CharField(
        "Название банка", max_length=250, blank=True, default="",
    )

    # @property
    # def is_valid_for_sign(self) -> bool:
    #     return (self.pro)

    def __str__(self):
        return self.name_of_provider


class UnitOfMeasurementOfSpecification(models.Model):
    unit = models.CharField("Единица измерения", max_length=250)

    def __str__(self):
        return self.unit


class SpecificationsOfProduct(models.Model):
    name = models.CharField(max_length=255)
    required = models.BooleanField(default=False)
    type = models.CharField(
        choices=SpecificationTypes.readable(), max_length=255
    )  # Enum
    unit_of_measurement = models.ForeignKey(
        UnitOfMeasurementOfSpecification,
        on_delete=models.CASCADE,
        related_name="unit_of_measurement",
    )
    description = models.TextField("Описание", blank=True, null=True)
    # min_value = models.IntegerField("Минимальное значение", blank=True, null=True)
    # is_edit_min_value = models.BooleanField(
    #     "Редактируемое минимальное значение?", blank=True, null=True
    # )
    # max_value = models.IntegerField("Максимальное значение", blank=True, null=True)
    # is_edit_max_value = models.BooleanField(
    #     "Редактируемое максимальное значение?", blank=True, null=True
    # )
    GOST = models.CharField("ГОСТ", max_length=250, blank=True, null=True)

    def __str__(self):
        return f"Спецификация  {self.name}"


class ProductSpecification(models.Model):
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="specification_values"
    )
    specification = models.ForeignKey(
        "SpecificationsOfProduct",
        on_delete=models.CASCADE,
        related_name="specification_values",
    )

    value = models.TextField(blank=True)


class Category(models.Model):
    name = models.CharField(max_length=255)
    specifications = models.ManyToManyField(
        SpecificationsOfProduct, blank=True, related_name="categories",
    )

    def __str__(self):
        return f"Категория: {self.name}"


class Product(models.Model):
    title = models.CharField("Название", max_length=250, null=True)
    description = models.TextField("Описание", blank=True, null=True)
    specifications = models.ManyToManyField(
        SpecificationsOfProduct, blank=True, related_name="specifications",
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    harvest_year = models.DateField("Год урожая", blank=True, null=True)
    harvest_type = models.CharField("Тип урожая", max_length=250, blank=True, null=True)

    def __str__(self):
        return self.title


class Warehouse(models.Model):
    title = models.CharField("Название", max_length=250, default="")
    address = models.CharField("Адрес", max_length=250, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")

    def __str__(self):
        return self.title


class WarehouseDistance(models.Model):
    # Todo: Added validation
    form = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name="starts")
    to = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name="ends")

    distance = models.IntegerField()
    price = models.IntegerField()


class Offer(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=250)
    volume = models.IntegerField(verbose_name="Объем")
    description = models.TextField("Описание", blank=True, default="")
    status = models.CharField(
        "Статус",
        max_length=250,
        choices=OfferStatus.readable(),
        default=OfferStatus.active.value,
    )
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField("Создано (время)", auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    date_start_shipment = models.DateTimeField(
        "Дата старта поставки", blank=True, null=True
    )
    date_finish_shipment = models.DateTimeField(
        "Дата окончания поставки", blank=True, null=True
    )
    cost = models.IntegerField()

    prices: Optional[list[DeliveryPrice]] = None

    objects = OfferQuerySet.as_manager()
    service = OfferManager()

    @property
    def cost_with_NDS(self):
        if self.cost:
            return self.cost + (self.cost * NDS / 100)
        else:
            return 0

    @property
    def cost_by_kg(self) -> Decimal:
        return Decimal(round(self.cost / self.volume))

    @property
    def period_of_export(self):
        if self.date_finish_shipment and self.date_start_shipment:
            delta = self.date_finish_shipment - self.date_start_shipment
            return delta.days
        else:
            return 0

    @property
    def days_till_end(self):
        if self.date_finish_shipment:
            res = datetime.now(timezone.utc) - self.date_finish_shipment
            return res.days if res.days >= 0 else 0
        return 0

    def __str__(self):
        if self.title:
            return self.title
        else:
            return str(self.id)


class Document(models.Model):
    name = models.CharField("Имя документа", max_length=250, default="")
    type_doc = models.CharField("Тип документа", max_length=250, null=True, blank=True)
    file = models.FileField("Файл", upload_to="uploads/%Y/%m/%d/%H/%M/%S", null=True)
    sign_file = models.FileField(
        "Файл подписи", upload_to="uploads/%Y/%m/%d/%H/%M/%S", null=True
    )


class CarsForShipment(models.Model):
    name = models.CharField(max_length=250)
    deliver = models.CharField(max_length=255)


class Shipment(models.Model):
    status = models.CharField(max_length=250)
    documents = models.ManyToManyField(Document)
    cars = models.ManyToManyField(CarsForShipment)


class Order(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name="orders")
    status = models.CharField(
        max_length=50, choices=OrderStatus.readable(), default=OrderStatus.new.value
    )
    provider = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="provider"
    )
    accepted_volume = models.IntegerField()
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="customer"
    )
    documents = models.ManyToManyField(Document)
    selected_warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

    name_of_contract = models.CharField(
        "Название договора", max_length=250, default="",
    )
    number_of_spec = models.CharField("Номер спецификации", max_length=250, default="",)
    date_start_of_spec = models.DateTimeField(
        "Дата начала спецификации", blank=True, null=True
    )
    date_finish_of_spec = models.DateTimeField(
        "Дата окончания спецификации", blank=True, null=True
    )
    date_start_of_contract = models.DateTimeField(
        "Дата начала договора", blank=True, null=True
    )
    date_finish_of_contract = models.DateTimeField(
        "Дата окончания договора", blank=True, null=True
    )

    date_start_shipment = models.DateTimeField(
        "Дата старта экспорта", blank=True, null=True
    )
    date_finish_shipment = models.DateTimeField(
        "Дата окончания экспорта", blank=True, null=True
    )
    amount_of_NDS = models.IntegerField("Размер НДС", default=0)


class RateForDelivery(models.Model):
    way = models.ForeignKey(
        WarehouseDistance, on_delete=models.CASCADE, related_name="rates"
    )
    cost_per_tonne = models.IntegerField("Стоимость за 1 тонну", blank=True, null=True)
    min = models.IntegerField(blank=True, null=True)
    max = models.IntegerField(blank=True, null=True)
    delta = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return "{}р за 1 тонну".format(self.cost_per_tonne)
