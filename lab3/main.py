#!/usr/bin/python3.7

"""main.py Contains all experiments for lab 3

For the ID2222 Data Mining course at KTH Royal Institute of Technology"""

__author__ = "Xenia Ioannidou and Bas Straathof"


from argparse import ArgumentParser, Namespace
from sys import argv
import networkx as nx
import statistics

from helpers import create_graph, get_graph_statistics
from reservoir_sampling import reservoir_sampling
from triest import Triest


def parse_args():
    """Parses CL arguments"""
    parser = ArgumentParser()

    parser.add_argument("-d", "--dataset", type=str, default="out.facebook-wosn-links")
    parser.add_argument("-m", "--M", type=int, default=50000,
            help="The number of edges in the reservoir.")
    parser.add_argument("-n", "--runs", type=int, default=20,
            help="How often you want to run the algorithm on the data set.")

    return parser.parse_args(argv[1:])


def main(args: Namespace):
    print(f"Dataset: {args.dataset}")
    print(f"M: {args.M}")
    print(f"n: {args.runs}")
    print("-"*20, "\n")

    # Create a graph from the data set
    G = create_graph(args.dataset)

    # Create a reservoir using the simple reservoir sampling algorithm
    S = reservoir_sampling(G, args.M)

    # Show some statistics of S
    print("Obtain statistics about about the reservoir.")
    get_graph_statistics(S)

    # Store all estimates of the global amount of triangles in a list
    estimates = []
    for i in range(args.runs):
        triest = Triest(G, args.M)
        S, tau = triest.triest_base()
        estimates.append(int(tau))
        print(f"Run {i}: {int(tau)}")

    print("\nApproximation of the global amount of triangles in the graph:")
    print(f"- mean estimate: {statistics.mean(estimates)}")
    print(f"- standard deviation: {statistics.stdev(estimates)}")


if __name__ == "__main__":
    main(parse_args())

