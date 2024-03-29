import datetime
import functools
import itertools
from collections import Iterable
from dataclasses import dataclass
from typing import Optional

from django.db.models import QuerySet, Sum, F, Case, When, CharField, Value

from .. import models
from ..enums import OfferStatus
from ..utils import get_data_of_cost_delivery


@dataclass
class DeliveryPrice:
    warehouse: "models.Warehouse"
    price_per_tonne: int
    price_per_tonne_with_nds: int


@dataclass
class OfferWithPrices:
    offer: "models.Offer"
    prices: list[DeliveryPrice]


@dataclass
class GroupedOffers:
    name: str
    offers: list[OfferWithPrices]


class OfferQuerySet(QuerySet):
    def ordered_by_type(self) -> QuerySet:
        return self.order_by("product__culture__category__id")

    def annotate_status(self):
        return self.annotate(
            accepted_volume=Sum(F("orders__accepted_volume"))
        ).annotate(
            status_sql=Case(
                When(
                    accepted_volume__gte=F("volume"),
                    then=Value(OfferStatus.archived.value),
                ),
                default=Value(OfferStatus.active.value),
                output_field=CharField(),
            )
        )

    def get_price_for(self, offer: "models.Offer", user):
        prices_data = get_data_of_cost_delivery(user, offer.warehouse, offer)
        prices = list(
            DeliveryPrice(
                warehouse=price["warehouse_from"],
                price_per_tonne=models.Order.price_service.farmer_price(
                    offer=offer, delivery_cost=price["cost_delivery_per_tonne"]
                ),
                price_per_tonne_with_nds=models.Order.price_service.farmer_price_with_nds(
                    offer=offer, delivery_cost=price["cost_delivery_per_tonne"]
                ),
            )
            for price in prices_data
        )
        return prices

    def iterator_grouped_by_harvest(self, user) -> Iterable[GroupedOffers]:
        def _get_harvest_type(offer):
            return functools.reduce(
                getattr, ("product", "culture", "category", "id"), offer
            )

        offers = self.annotate_status().ordered_by_type().filter(status_sql="active")
        for k, g in itertools.groupby(offers, _get_harvest_type):
            any_: Optional["models.Offer"] = None
            group_offers = []
            for offer in g:
                any_ = offer
                prices = self.get_price_for(offer, user)
                group_offers.append(OfferWithPrices(offer=offer, prices=prices))
            yield GroupedOffers(
                offers=group_offers, name=any_.product.culture.category.name
            )
