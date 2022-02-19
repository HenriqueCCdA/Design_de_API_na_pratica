def now():
    from django.utils.datetime_safe import datetime
    return datetime.now()


class DoesNotExist(Exception):
    pass


class Order:
    def __init__(self, coffee='', size='', milk='', location='', id=None, created_at=None, status=None):
        self.id = None if id is None else int(id)
        self.coffee = coffee
        self.size = size
        self.milk = milk
        self.location = location
        self.created_at = now() if created_at is None else created_at
        #self.status =


class CoffeeShop:
    def __init__(self):
        self.orders = {}

    def place_order(self, order):
        if order.id is None:
            order.id = len(self.orders) + 1

        self.orders[order.id] = order

        return order

    def delete(self, order):
        try:
            return self.orders.pop(order.id)
        except KeyError as e:
            raise DoesNotExist(order.id)

    def update(self, order):
        if order.id not in self.orders:
            raise DoesNotExist(order.id)
        self.orders[order.id] = order
        return order

    def read(self, id):
        id = int(id)
        try:
            return self.orders[int(id)]
        except KeyError as e:
            raise DoesNotExist(id)
