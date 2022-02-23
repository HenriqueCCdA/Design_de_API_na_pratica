from http import HTTPStatus
import httpretty

from client_level1.client import create_order, delete_order, read_order, update_order


@httpretty.activate
def test_create():
    httpretty.register_uri(
        httpretty.POST,
        'http://localhost:8000/order/create?coffee=latte&size=large&milk=whole&location=takeAway',
        'coffee=latte\nid=1\nlocation=takeAwey\nmilk=whole\nsize=large',
        status=HTTPStatus.CREATED,
        match_querystring=True
    )

    assert create_order('latte', 'large', 'whole', 'takeAway') == 1


@httpretty.activate
def test_delete():
    httpretty.register_uri(
        httpretty.POST,
        'http://localhost:8000/order/delete?id=1',
        status=HTTPStatus.NO_CONTENT,
        match_querystring=True
    )

    assert delete_order(id=1)


@httpretty.activate
def test_read():
    httpretty.register_uri(
        httpretty.GET,
        'http://localhost:8000/order/read?id=1',
        'coffee=latte\nid=1\nlocation=takeAway\nmilk=whole\nsize=large',
        status=HTTPStatus.OK,
        match_querystring=True
    )

    assert read_order(id=1) == {
        'coffee':'latte',
        'id': '1',
        'location': 'takeAway',
        'milk': 'whole',
        'size': 'large'
    }


@httpretty.activate
def test_update():
    httpretty.register_uri(
        httpretty.POST,
        'http://localhost:8000/order/update?coffee=latte&id=1&size=large&milk=whole&location=dinein',
        'coffee=latte\nid=1\nlocation=dinein\nmilk=whole\nsize=large',
        status=HTTPStatus.OK,
        match_querystring=True
    )

    assert update_order(1, 'latte', 'large', 'whole', 'dinein') == {
        'coffee': 'latte',
        'id': '1',
        'location': 'dinein',
        'milk': 'whole',
        'size': 'large'
    }