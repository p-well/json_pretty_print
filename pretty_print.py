import argparse

from os.path import exists
from json import dumps, load


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path')
    return parser


def check_args(parser, args):
    if not exists(args.path):
        parser.error('File not found.')


def read_json_file(path):
    with open(path, mode='r', encoding='utf-8') as deserialized_fp:
        return load(deserialized_fp)


def prettify_print(deserialized_fp):
    return dumps(deserialized_fp, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    check_args(parser, args)
    deserialized_fp = read_json_file(args.path)
    serialized_prettified_fp = prettify_print(deserialized_fp)
    print(serialized_prettified_fp)
