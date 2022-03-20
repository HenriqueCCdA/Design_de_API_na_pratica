from http import HTTPStatus

import pytest

from coffeeApi.level3.domain import Status


def test_delete_success(api_client, one_coffee):
    url = '/receipt/1'

    response = api_client.delete(url)

    assert response.status_code == HTTPStatus.NO_CONTENT
    assert len(one_coffee.orders) == 1
    assert one_coffee.read(1).is_collected()


@pytest.mark.skip
def test_delete_badreq(client, one_coffee):
    url = '/receipt'

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

    url = '/receipt/404'

    reponse = api_client.delete(url)

    assert reponse.status_code == HTTPStatus.NOT_FOUND
    assert len(one_coffee.orders) == 1


def test_receipt_already_delivered(api_client, one_coffee):

    one_coffee.read(1).status = Status.Collected

    url = '/receipt/1'

    response = api_client.delete(url)

    assert response.status_code == HTTPStatus.CONFLICT
