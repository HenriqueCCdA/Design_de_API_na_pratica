import pytest

from coffeeApi.level1.domain import CoffeeShop, Order


@pytest.fixture
def coffeeshop(mocker):
    cs = CoffeeShop()
    mocker.patch('coffeeApi.level1.views.coffeeshop', cs)
    return cs

@pytest.fixture
def order():
    return Order(coffee='latte', size='large', milk='whole', location='takeAway')

@pytest.fixture
def one_coffee(coffeeshop, order):
    # coffee=latte&size=large&milk=whole&location=takeAwey
    coffeeshop.place_order(order)
    return coffeeshop
