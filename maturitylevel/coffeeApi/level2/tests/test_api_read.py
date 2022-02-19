from http import HTTPStatus

import pytest


def test_read_success(api_client, one_coffee):
    url = '/order/1'

    response = api_client.get(url)

    assert response.status_code == HTTPStatus.OK
    assert response.content  == b'coffee=latte\nid=1\nlocation=takeAway\nmilk=whole\nsize=large'


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
