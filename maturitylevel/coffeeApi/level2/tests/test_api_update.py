from http import HTTPStatus

import pytest

def test_update_sucess(api_client, one_coffee):
    url = '/order/1'

    data = dict(coffee='curto', milk='', size='small', location='takeAway')

    response = api_client.put(url, data=data)

    assert response.status_code == HTTPStatus.NO_CONTENT
    assert len(one_coffee.orders) == 1
    assert (dict(coffee='curto', milk='', size='small', id=1, location='takeAway')
        == vars(one_coffee.read(1))
    )

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
