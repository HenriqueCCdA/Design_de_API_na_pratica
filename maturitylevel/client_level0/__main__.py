import argparse

from client_level0.core import place_order

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

print(place_order(args.coffee, args.size, args.milk, args.location))