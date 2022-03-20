from datetime import datetime
from http import HTTPStatus
import pstats

import pytest
from coffeeApi.level3.domain import Status

from coffeeApi.level3.views import payment


def test_read_success(api_client, one_coffee):
    url = '/order/1'

    response = api_client.get(url)

    assert response.status_code == HTTPStatus.OK

    links = dict(
        self='http://testserver/order/1',
        update='http://testserver/order/1',
        cancel='http://testserver/order/1',
        payment='http://testserver/payment/1'
    )

    excepted = dict(coffee='latte', milk='whole', size='large', id=1, location='takeAway',
                    created_at=datetime(2021, 4, 28), status="Placed", links=links)
    assert response.json() == excepted


def test_read_paid_links(api_client, one_coffee):
    one_coffee.read(1).status = Status.Paid

    url = '/order/1'

    response = api_client.get(url)

    assert response.json()['links'] == dict(self='http://testserver/order/1')


def test_read_served_links(api_client, one_coffee):
    one_coffee.read(1).status = Status.Served

    url = '/order/1'

    response = api_client.get(url)

    assert response.json()['links'] == dict(self='http://testserver/order/1',
                                            receipt='http://testserver/receipt/1')


@pytest.mark.skip
def test_read_not_allowed(api_client, one_coffee):
    url = '/order/1'

    response = api_client.post(url)

    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED

@pytest.mark.skip
def test_read_beadreq(api_client, one_coffee):
    url = '/order'

    response = api_client.get(url)

    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_read_not_found(api_client, one_coffee):

    url = '/order/404'

    response = api_client.get(url)

    assert response.status_code == HTTPStatus.NOT_FOUND
