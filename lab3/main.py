#!/usr/bin/python3.7

"""main.py Contains all experiments for lab 3

For the ID2222 Data Mining course at KTH Royal Institute of Technology"""

__author__ = "Xenia Ioannidou and Bas Straathof"


from argparse import ArgumentParser, Namespace
from sys import argv

from helpers import load_dataset


def parse_args():
    """Parses CL arguments"""
    parser = ArgumentParser()

    parser.add_argument("-d", "--dataset", type=str, default="toy.csv")

    return parser.parse_args(argv[1:])


def main(args: Namespace):
    df = load_dataset(args.dataset)

if __name__ == "__main__":
    main(parse_args())
