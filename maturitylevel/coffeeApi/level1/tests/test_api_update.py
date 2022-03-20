from http import HTTPStatus


def test_update_sucess(client, one_coffee):
    url = 'http://localhost:8000/order/update?id=1&coffee=curto&size=small&milk=&location=takeAway'

    response = client.post(url)

    assert response.status_code == HTTPStatus.OK
    assert len(one_coffee.orders) == 1
    assert (dict(coffee='curto', milk='', size='small', id=1, location='takeAway')
        == vars(one_coffee.read(1))
    )


def test_update_not_allowed(client, one_coffee):
    url = 'http://localhost:8000/order/update?id=1&coffee=curto&size=small&milk=&location=takeAway'

    response = client.get(url)

    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED


def test_update_badreq(client):
    url = 'http://localhost:8000/order/update?id=1'

    response = client.post(url)

    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_update_not_found(client):
    url = 'http://localhost:8000/order/update?id=404&coffee=curto&size=small&milk=&location=takeAway'

    response = client.post(url)

    assert response.status_code == HTTPStatus.NOT_FOUND
