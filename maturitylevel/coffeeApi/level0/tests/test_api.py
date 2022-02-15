import pytest
from coffeeApi.level0.domain import CoffeeShop


@pytest.fixture
def coffeeshop(mocker):
    cs = CoffeeShop()
    mocker.patch('coffeeApi.level0.views.coffeeshop', cs)
    return cs


def test_get(client, coffeeshop):
    url = 'http://localhost:8000/PlaceOrder?coffee=latte&size=large&milk=whole&location=takeAwey'

    response = client.get(url)

    assert len(coffeeshop.orders) == 1
    assert b'Order=1' == response.content


def test_post(client, coffeeshop):
    url = 'http://localhost:8000/PlaceOrder?coffee=latte&size=large&milk=whole&location=takeAwey'

    response = client.post(url)

    assert len(coffeeshop.orders) == 1
    assert b'Order=1' == response.content