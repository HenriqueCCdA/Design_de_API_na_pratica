from http import HTTPStatus

from coffeeApi.level3.domain import Status


def test_payment_success(api_client, one_coffee):
    url = '/payment/1'

    data = dict(amount=199)
    response = api_client.put(url, data=data)

    assert response.status_code == HTTPStatus.OK

    links = dict(self='http://testserver/order/1')

    excepted = dict(links=links)

    assert response.json() == excepted
    assert len(one_coffee.orders) == 1


def test_payment_badreq(api_client, one_coffee):
    url = '/payment/1'

    data = dict()

    response = api_client.put(url, data=data)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert len(one_coffee.orders) == 1
    assert not one_coffee.read(1).is_paid()


def test_payment_not_found(api_client):
    url = '/payment/404'

    data = dict(amount='199')
    response = api_client.put(url, data=data)

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_payment_already_paid(api_client, one_coffee):

    one_coffee.read(1).status = Status.Paid

    url = '/payment/1'

    data = dict(amount='199')

    response = api_client.put(url, data=data)

    assert response.status_code == HTTPStatus.CONFLICT