import json

import pytest as pytest
from rest_framework.test import APIClient
from model_bakery import baker

from service_order.models import User, Shop


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user_factory():
    def factory(*args, **kwargs):
        return baker.make(User, *args, **kwargs)

    return factory


@pytest.fixture
def shop_factory():
    def factory(*args, **kwargs):
        return baker.make(Shop, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_search_products(client):
    response = client.get(f"/api/products/search_products/")

    assert response.status_code == 200


@pytest.mark.django_db
def test_search_category(client):
    response = client.get(f"/api/categories/")

    assert response.status_code == 200


@pytest.mark.django_db
def test_new_user(client, user_factory):
    user = user_factory(_quantity=1)
    data = {
        "email": user[0].email,
        "password": user[0].password,
    }
    response = client.post(f"/api/user/user_register/", content_type="application/json", data=json.dumps(data))

    assert response.status_code == 200


@pytest.mark.django_db
def test_get_shop_state(client, shop_factory):
    shop = shop_factory(_quantity=1)

    response = client.get(f"/api/shops/")

    assert response.status_code == 200
    data = response.json()
    assert shop[0].name == data[0]['name']


@pytest.mark.django_db
def test_update_price(client):
    response = client.post(f"/api/shops/update_price/")

    assert response.status_code == 403
    data = response.json()
    assert data['Error'] == 'Log in required'


@pytest.mark.django_db
def test_user_register(client):
    user_data = {
        "first_name": "test",
        "last_name": "test_name",
        "email": 'test@example.com',
        "password": 'test12345',
        "company": "test_company",
        "position": "test_position"
    }
    response = client.post(f"/api/user/user_register/", content_type="application/json", data=json.dumps(user_data))

    assert response.status_code == 200
    data = response.json()
    assert data['Status']
