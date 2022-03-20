from datetime import datetime
from http import HTTPStatus

import pytest

def test_update_sucess(api_client, one_coffee):
    url = '/order/1'

    data = dict(coffee='curto', milk='', size='small', location='takeAway')

    response = api_client.put(url, data=data)

    links = dict(
        self='http://testserver/order/1',
        update='http://testserver/order/1',
        cancel='http://testserver/order/1',
        payment='http://testserver/payment/1'
    )

    expected = dict(coffee='curto', milk='', size='small', id=1, location='takeAway',
               created_at=datetime(2021, 4, 28), status='Placed', links=links)

    assert response.status_code == HTTPStatus.OK
    assert len(one_coffee.orders) == 1
    assert expected == response.json()

@pytest.mark.skip
def test_update_not_allowed(client, one_coffee):
    url = '/order?id=1&coffee=curto&size=small&milk=&location=takeAway'

    response = client.get(url)

    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED


def test_update_badreq(api_client):
    url = '/order/1'

    data = dict(coffee='curto', milk='', location='takeAway')

    response = api_client.put(url, data=data)

    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_update_not_found(api_client):
    url = '/order/404'

    data = dict(coffee='curto', milk='', size='small', location='takeAway')
    response = api_client.put(url, data=data)

    assert response.status_code == HTTPStatus.NOT_FOUND
