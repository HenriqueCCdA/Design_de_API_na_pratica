from http import HTTPStatus


def test_delete_success(client, one_coffee):
    url = '/order/delete?id=1'

    response = client.post(url)

    assert response.status_code == HTTPStatus.NO_CONTENT
    assert len(one_coffee.orders) == 0


def test_delete_badreq(client, one_coffee):
    url = '/order/delete'

    reponse = client.post(url)

    assert reponse.status_code == HTTPStatus.BAD_REQUEST
    assert len(one_coffee.orders) == 1


def test_delete_not_allowed(client, one_coffee):
    url = '/order/delete?id=1'

    reponse = client.get(url)

    assert reponse.status_code == HTTPStatus.METHOD_NOT_ALLOWED
    assert len(one_coffee.orders) == 1

def test_delete_not_found(client, one_coffee):

    url = '/order/delete?id=404'

    reponse = client.post(url)

    assert reponse.status_code == HTTPStatus.NOT_FOUND
    assert len(one_coffee.orders) == 1
