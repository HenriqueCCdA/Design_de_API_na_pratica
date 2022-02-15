from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

from coopy.base import init_persistent_system

from coffeeApi.level0.domain import CoffeeShop, Order


coffeeshop = init_persistent_system(CoffeeShop(), basedir='data/level0')


def barista(request):
    '''
    http://localhost:8000/PlaceOrder?coffee=latte&size=large&milk=whole&location=takeAwey
    '''

    try:
        params = {k: request.GET[k] for k in ('coffee', 'size', 'milk', 'location')}
    except MultiValueDictKeyError as e:
        status = 400
        headers = {'Content-Type': 'text/plain; charset=utf-8'}
        body = str(e).strip("'")
        return HttpResponse(body, status=status, headers=headers)

    order = Order(**params)
    coffeeshop.place_order(order)

    body = f'Order={order.id}'
    headers = {'Content-Type': 'text/plain; charset=utf-8'}

    return HttpResponse(body, headers=headers)
