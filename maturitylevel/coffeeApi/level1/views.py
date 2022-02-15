from coopy.base import init_persistent_system

from coffeeApi.level1.domain import CoffeeShop, Order, serialize
from coffeeApi.level1.framework import Ok, allow, Created, NoContent, require


coffeeshop = init_persistent_system(CoffeeShop(), basedir='data/level1')

@allow(['POST'])
@require('coffee', 'size', 'milk', 'location')
def create(request, params):

    order = Order(**params)
    coffeeshop.place_order(order)

    return Created(serialize(order))


@allow(['POST'])
@require('id')
def delete(request, params):

    order = Order(**params)
    coffeeshop.delete(order)

    return NoContent()


@allow(['POST'])
@require('id', 'coffee', 'size', 'milk', 'location')
def update(request, params):

    order = Order(**params)
    order = coffeeshop.update(order)

    return NoContent()


@allow(['GET'])
@require('id')
def read(request, params):

    order = coffeeshop.read(**params)

    body = serialize(order)

    return Ok(body)
