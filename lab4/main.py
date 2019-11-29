#!/usr/bin/python3.7

"""main.py Contains all experiments for lab 4

For the ID2222 Data Mining course at KTH Royal Institute of Technology"""

__author__ = "Xenia Ioannidou and Bas Straathof"


from argparse import ArgumentParser, Namespace
from sys import argv
from sklearn import cluster

from helpers import *
from k_eigenvector import k_eigenvector


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

    print("Obtain statistics about about the graph...")
    get_graph_statistics(G)

    # Perform the k_eigenvector algorithm
    k, labels = k_eigenvector(G, plot=True, save=True, gid=args.dataset[:-4])

    print(f"The optimal number of clusters is: {k}\n")

    # Draw the clustered graph
    draw_graph(G, labels=False, colors=labels)


if __name__ == "__main__":
    main(parse_args())

