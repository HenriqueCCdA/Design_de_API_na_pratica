from http import HTTPStatus


def test_get_not_allowed(client, coffeeshop):
    url = 'http://localhost:8000/order/create?coffee=latte&size=large&milk=whole&location=takeAwey'

    response = client.get(url)

    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED
    assert len(coffeeshop.orders) == 0


def test_post_sucess(client, coffeeshop):
    url = 'http://localhost:8000/order/create?coffee=latte&size=large&milk=whole&location=takeAwey'

    response = client.post(url)

    assert response.status_code == HTTPStatus.CREATED
    assert len(coffeeshop.orders) == 1
    assert response.content == b'coffee=latte\nid=1\nlocation=takeAwey\nmilk=whole\nsize=large'


def test_post_badreq(client, coffeeshop):
    url = 'http://localhost:8000/order/create?coffee=latte&size=large&milk=whole'

    response = client.post(url)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert len(coffeeshop.orders) == 0
