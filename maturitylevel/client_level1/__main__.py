import argparse
import json
import requests



BASE_URL = 'http://localhost:8000'


def post(coffee, size, milk, location):
    url = f'{BASE_URL}/order'

    data = dict(coffee='latte', milk='whole', size='large', location='takeAway')

    headers = {'content-type': 'application/json'}

    r = requests.post(url, data=json.dumps(data), headers=headers)

    return r.headers['Location']

def get(url):

    headers = {'content-type': 'application/json'}
    r = requests.get(url, headers=headers)

    return r.json()

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

parser = build_parser()
args = parser.parse_args()

print(get(post(args.coffee, args.size, args.milk, args.location)))