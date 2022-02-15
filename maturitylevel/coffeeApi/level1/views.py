from http import HTTPStatus
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

from coopy.base import init_persistent_system

from coffeeApi.level1.domain import CoffeeShop, DoesNotExist, Order
from coffeeApi.level1.framework import MyResponse, allow, BadRequest, Created, MethodNotAllewed, NoContent, NotFound, require


coffeeshop = init_persistent_system(CoffeeShop(), basedir='data/level1')

@allow(['POST'])
@require('coffee', 'size', 'milk', 'location')
def create(request, params):

    order = Order(**params)
    coffeeshop.place_order(order)

    body = f'Order={order.id}'

    return Created(body)


@allow(['POST'])
@require('id')
def delete(request, params):

    try:
        order = Order(**params)
        coffeeshop.delete(order)
    except DoesNotExist as e:
        return NotFound()

    return NoContent()


@allow(['POST'])
@require('id', 'coffee', 'size', 'milk', 'location')
def update(request, params):

    try:
        order = Order(**params)
        order = coffeeshop.update(order)
    except DoesNotExist as e:
        return NotFound()

    return NoContent()


@allow(['GET'])
@require('id')
def read(request, params):

    try:
        order = coffeeshop.read(**params)
    except DoesNotExist as e:
        return NotFound()

    return MyResponse(str(order))
