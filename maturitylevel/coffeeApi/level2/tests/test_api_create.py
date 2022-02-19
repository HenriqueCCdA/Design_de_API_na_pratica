from http import HTTPStatus

import pytest

@pytest.mark.skip
def test_get_not_allowed(client, coffeeshop):
    url = '/order?coffee=latte&size=large&milk=whole&location=takeAwey'

    data = dict(coffee='latte', size='large', milk='whole', location='takeAwey')

    response = client.get(url, data=data)

    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED
    assert len(coffeeshop.orders) == 0


def test_post_sucess(api_client, coffeeshop):
    url = '/order'

    data = dict(coffee='latte', size='large', milk='whole', location='takeAwey')

    response = api_client.post(url, data=data)

    assert response.status_code == HTTPStatus.CREATED
    assert len(coffeeshop.orders) == 1
    #assert response.content == b'coffee=latte\nid=1\nlocation=takeAwey\nmilk=whole\nsize=large'

    expected = dict(id=1, coffee='latte', size='large', milk='whole', location='takeAwey')
    assert response.json() == expected


def test_post_badreq(api_client, coffeeshop):
    url = '/order'

    data = dict(coffee='latte', size='large', location='takeAwey')

    response = api_client.post(url, data=data)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert len(coffeeshop.orders) == 0
