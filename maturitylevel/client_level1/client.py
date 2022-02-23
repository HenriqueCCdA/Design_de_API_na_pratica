from http import HTTPStatus
import requests


BASE_URL = 'http://localhost:8000'


def deserialize(body):
    return {k: v for k, v in [item.split('=') for item in body.split()]}


def create_order(coffee, size, milk, location):
    url = f'{BASE_URL}/order/create'

    params = {'coffee': coffee, 'size': size, 'milk': milk, 'location': location}

    r = requests.post(url, params=params, headers={'Content-Type': 'text/plain'})

    order = deserialize(r.text)

    return int(order['id'])


def delete_order(id):
    url = f'{BASE_URL}/order/delete'

    params = {'id': id}

    r = requests.post(url, params=params, headers={'Content-Type': 'text/plain'})

    return r.status_code == HTTPStatus.NO_CONTENT


def read_order(id):
    url = f'{BASE_URL}/order/read'

    params = {'id': id}
    r = requests.get(url, params=params, headers={'Content-Type': 'text/plain'})

    return deserialize(r.text)


def update_order(id, coffee, size, milk, location):
    url = f'{BASE_URL}/order/update'

    params = {'coffee': coffee, 'id': id, 'size': size, 'milk': milk, 'location': location}

    r = requests.post(url, params=params, headers={'Content-Type': 'text/plain'})

    order = deserialize(r.text)

    return order