import json

import pytest
from django.urls import reverse
from model_bakery import baker

from main import models


@pytest.fixture()
def offer():
    return baker.make("main.Offer")


@pytest.mark.django_db(transaction=True)
def test_offer_creating(client, admin_token, products):
    response = client.post(
        reverse("offer-list"),
        content_type="application/json",
        data=json.dumps({"cost": 100, "volume": 10}),
        HTTP_AUTHORIZATION=f"Bearer {admin_token}",
    )
    assert response.status_code == 201
    assert response.json()
    assert models.Offer.objects.count() == 1

    response = client.post(
        reverse("offer-list"),
        content_type="application/json",
        data=json.dumps(
            {
                "cost": 100,
                "volume": 10,
                "product": {"id": models.Product.objects.first().id},
            }
        ),
        HTTP_AUTHORIZATION=f"Bearer {admin_token}",
    )
    assert response.status_code == 201
    assert response.json()
    assert models.Offer.objects.count() == 2


@pytest.mark.django_db(transaction=True)
def test_offer_patching(client, offer: models.Offer, products, admin_token):
    response = client.patch(
        reverse("offer-detail", kwargs={"pk": offer.id}),
        content_type="application/json",
        data=json.dumps({"product": {"id": models.Product.objects.first().id}}),
        HTTP_AUTHORIZATION=f"Bearer {admin_token}",
    )
    assert response.status_code == 200
    assert response.json()
    assert models.Offer.objects.count() == 1
    assert models.Offer.objects.first().product_id == models.Product.objects.first().id


@pytest.mark.django_db(transaction=True)
def test_offer_grouped(client, offer_groping_case, admin_token):
    res = client.get(
        reverse("offer-grouped"), HTTP_AUTHORIZATION=f"Bearer {admin_token}",
    )
    assert res.status_code == 200