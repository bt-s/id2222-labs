#!/usr/bin/python3.7

"""main.py Contains all experiments for lab 4

For the ID2222 Data Mining course at KTH Royal Institute of Technology"""

__author__ = "Xenia Ioannidou and Bas Straathof"


from argparse import ArgumentParser, Namespace
from sys import argv

from helpers import *


def parse_args():
    """Parses CL arguments"""
    parser = ArgumentParser()

    parser.add_argument("-d", "--dataset", type=str,
            default="example1.dat")

    return parser.parse_args(argv[1:])


def main(args: Namespace):
    print(f"Dataset: {args.dataset}")
    print("-"*20, "\n")

    # Create a graph from the data set
    G = create_graph(args.dataset)

if __name__ == "__main__":
    main(parse_args())

