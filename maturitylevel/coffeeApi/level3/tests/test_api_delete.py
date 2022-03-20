from http import HTTPStatus

import pytest


def test_delete_success(api_client, one_coffee):
    url = '/order/1'

    response = api_client.delete(url)

    assert response.status_code == HTTPStatus.NO_CONTENT
    assert len(one_coffee.orders) == 1
    assert one_coffee.read(1).is_cancelled()


@pytest.mark.skip
def test_delete_badreq(client, one_coffee):
    url = '/order'

    reponse = client.delete(url)

    assert reponse.status_code == HTTPStatus.BAD_REQUEST
    assert len(one_coffee.orders) == 1

@pytest.mark.skip
def test_delete_not_allowed(client, one_coffee):
    url = '/order?id=1'

    reponse = client.delete(url)

    assert reponse.status_code == HTTPStatus.METHOD_NOT_ALLOWED
    assert len(one_coffee.orders) == 1

def test_delete_not_found(api_client, one_coffee):

    url = '/order/404'

    reponse = api_client.delete(url)

    assert reponse.status_code == HTTPStatus.NOT_FOUND
    assert len(one_coffee.orders) == 1
