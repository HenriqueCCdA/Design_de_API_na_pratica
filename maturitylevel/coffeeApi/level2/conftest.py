import pytest
from pytest_django.lazy_django import skip_if_no_django


from coffeeApi.level2.domain import CoffeeShop, Order, Status
from coffeeApi.level2.framework import APIClient


@pytest.fixture
def coffeeshop(mocker):
    cs = CoffeeShop()
    mocker.patch('coffeeApi.level2.views.coffeeshop', cs)
    return cs

@pytest.fixture
def order():
    return Order(coffee='latte', size='large', milk='whole', location='takeAway', status=Status.Placed)

@pytest.fixture
def one_coffee(coffeeshop, order):
    # coffee=latte&size=large&milk=whole&location=takeAwey
    coffeeshop.place_order(order)
    return coffeeshop

@pytest.fixture
def api_client():
    skip_if_no_django()

    return APIClient()


@pytest.fixture(autouse=True)
def fixed_now(monkeypatch):
    from coffeeApi.level2 import domain
    from datetime import datetime
    monkeypatch.setattr(domain, 'now', lambda: datetime(2021, 4, 28))
