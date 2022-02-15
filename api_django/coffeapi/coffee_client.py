'''
TODO LIST:

- quem é o client
- os dados do pedido
- montar url
- fazer um get
- imprimir o id do pedido

'''

import argparse
import requests
import re


BASE_URL = 'http://localhost:8000'

def place_order(coffee, size, milk, location):
    url = f'{BASE_URL}/PlaceOrder?coffee={coffee}&size={size}&milk={milk}&location={location}'

    r = requests.get(url)

    order_id = ''.join(re.findall(r'Order=(\d+)', r.text))

    return order_id


def build_parser():
    parser =argparse.ArgumentParser()
    subparses = parser.add_subparsers(dest='command')
    subparses.required = True

    sp_order = subparses.add_parser('order')
    sp_order.add_argument('coffee')
    sp_order.add_argument('size')
    sp_order.add_argument('milk')
    sp_order.add_argument('location')

    return parser

if __name__ == '__main__':

    parser = build_parser()
    args = parser.parse_args()

    print(place_order(args.coffee, args.size, args.milk, args.location))