from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

from coopy.base import init_persistent_system

from domain import CoffeShop, Order


coffeShop = init_persistent_system(CoffeShop())


def barista(request):
    '''
    http://localhost:8000/PlaceOrder?coffee=latte&size=large&milk=whole&location=takeAwey
    '''

    try:
        params = {k: request.GET[k] for k in ('coffee', 'size', 'milk', 'location')}
    except MultiValueDictKeyError as e:
        key = str(e).strip("'")
        body = f'Missing Param: {key}'
        headers = {'Content-Type': 'text/plain; charset=utf-8'}
        return HttpResponse(body, status=400, headers=headers)

    order = Order(**params)
    coffeShop.place_order(order)

    body = f'Order={order.id}'
    headers = {'Content-Type': 'text/plain; charset=utf-8'}

    return HttpResponse(body, headers=headers)
