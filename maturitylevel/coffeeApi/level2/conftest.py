import pytest
from pytest_django.lazy_django import skip_if_no_django


from coffeeApi.level2.domain import CoffeeShop, Order
from coffeeApi.level2.framework import APIClient


@pytest.fixture
def coffeeshop(mocker):
    cs = CoffeeShop()
    mocker.patch('coffeeApi.level2.views.coffeeshop', cs)
    return cs

@pytest.fixture
def order():
    return Order(coffee='latte', size='large', milk='whole', location='takeAway')

@pytest.fixture
def one_coffee(coffeeshop, order):
    # coffee=latte&size=large&milk=whole&location=takeAwey
    coffeeshop.place_order(order)
    return coffeeshop

@pytest.fixture
def api_client():
    skip_if_no_django()

    return APIClient()
