import argparse


def build_parser():
    parser =argparse.ArgumentParser()
    subparses = parser.add_subparsers(dest='command')
    subparses.required = True

    sp_create = subparses.add_parser('create')
    sp_create.add_argument('coffee')
    sp_create.add_argument('size')
    sp_create.add_argument('milk')
    sp_create.add_argument('location')

    sp_update = subparses.add_parser('update')
    sp_update.add_argument('id')
    sp_update.add_argument('coffee')
    sp_update.add_argument('size')
    sp_update.add_argument('milk')
    sp_update.add_argument('location')

    sp_delete = subparses.add_parser('delete')
    sp_delete.add_argument('id')

    sp_read = subparses.add_parser('read')
    sp_read.add_argument('id')

    return parser
