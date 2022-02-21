from datetime import datetime
from http import HTTPStatus

import pytest

from coffeeApi.level2.framework import deserialize


@pytest.mark.skip
def test_get_not_allowed(client, coffeeshop):
    url = '/order?coffee=latte&size=large&milk=whole&location=takeAwey'

    data = dict(coffee='latte', size='large', milk='whole', location='takeAwey')

    response = client.get(url, data=data)

    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED
    assert len(coffeeshop.orders) == 0


def test_post_sucess(api_client, coffeeshop):
    url = '/order'

    data = dict(coffee='latte', size='large', milk='whole', location='takeAwey')

    response = api_client.post(url, data=data)

    assert response.status_code == HTTPStatus.CREATED
    assert response.headers['Location'] == 'http://testserver/order/1'
    assert len(coffeeshop.orders) == 1

    expected = dict(id=1, coffee='latte', size='large', milk='whole', location='takeAwey',
                    created_at=datetime(2021, 4, 28), status="Placed")

    assert deserialize(response.json()) == expected


def test_post_badreq(api_client, coffeeshop):
    url = '/order'

    data = dict(coffee='latte', size='large', location='takeAwey')

    response = api_client.post(url, data=data)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert len(coffeeshop.orders) == 0
