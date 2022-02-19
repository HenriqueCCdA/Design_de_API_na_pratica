from datetime import datetime
from http import HTTPStatus

import pytest

from coffeeApi.level2.framework import deserialize


def test_read_success(api_client, one_coffee):
    url = '/order/1'

    response = api_client.get(url)

    assert response.status_code == HTTPStatus.OK
    excepted = dict(coffee='latte', milk='whole', size='large', id=1, location='takeAway',
                    created_at=datetime(2021, 4, 28))
    assert deserialize(response.content) == excepted


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
