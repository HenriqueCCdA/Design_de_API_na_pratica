from http import HTTPStatus


def test_read_success(client, one_coffee):
    url = '/order/read?id=1'

    response = client.get(url)

    assert response.status_code == HTTPStatus.OK
    assert response.content  == b'coffee=latte\nid=1\nlocation=takeAway\nmilk=whole\nsize=large'


def test_read_not_allowed(client, one_coffee):
    url = '/order/read?id=1'

    response = client.post(url)

    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED


def test_read_beadreq(client, one_coffee):
    url = '/order/read'

    response = client.get(url)

    assert response.status_code == HTTPStatus.BAD_REQUEST

def test_read_not_found(client, one_coffee):

    url = '/order/read?id=404'

    response = client.get(url)

    assert response.status_code == HTTPStatus.NOT_FOUND
