from coopy.base import init_persistent_system

from coffeeApi.level2.domain import CoffeeShop, Order
from coffeeApi.level2.framework import Ok, allow, Created, NoContent, data_required, serialize


coffeeshop = init_persistent_system(CoffeeShop(), basedir='data/level2')

@allow(['GET', 'POST', 'PUT', 'DELETE'])
def dispatch(request, *args, **kwargs):
    methods = dict(GET=read, POST=create, PUT=update, DELETE=delete)

    view = methods[request.method]

    return view(request, *args, **kwargs)


@allow(['POST'])
@data_required('coffee', 'size', 'milk', 'location')
def create(request, params=None):

    order = Order(**params)
    coffeeshop.place_order(order)

    return Created(serialize(order))


@allow(['DELETE'])
def delete(request, id):

    order = Order(id=id)
    coffeeshop.delete(order)

    return NoContent()


@allow(['PUT'])
@data_required('coffee', 'size', 'milk', 'location')
def update(request, id, params=None):

    order = Order(id=id, **params)
    order = coffeeshop.update(order)

    return NoContent()


@allow(['GET'])
def read(request, id):

    order = coffeeshop.read(id=id)

    body = serialize(order)

    return Ok(body)
