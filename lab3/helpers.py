#!/usr/bin/python3

"""helpers.py Contains helper functions for lab 2

For the ID2222 Data Mining course at KTH Royal Institute of Technology"""

__author__ = "Xenia Ioannidou and Bas Straathof"


import networkx as nx
from networkx.classes.graph import Graph
from networkx.drawing.nx_pylab import draw_networkx
import matplotlib.pyplot as plt


def create_graph(f_name: str, n=2, sep=" ") -> Graph:
    Data = open(f_name, "r")
    for i in range(n):
        next(Data, None) # Delete a line in the input file

    # Define the graph type
    Graphtype = nx.Graph()

    # Define the graph
    G = nx.parse_edgelist(Data, delimiter=sep, create_using=Graphtype,
            nodetype=int)

    return G


def draw_graph(G, labels=True):
    draw_networkx(G, with_labels=labels, node_color="lightblue")
    plt.show()


def get_graph_statistics(G):
    print(f"\nThe number of edges is: {len(G.edges)}")
    print(f"\nThe number of nodes is: {len(G.nodes)}")

    # Find all cliques
    all_cliques = nx.enumerate_all_cliques(G)
    # Find all triangles
    triad_cliques = [x for x in all_cliques if len(x)==3 ]
    print(f"\nThe number of triangles is: {len(triad_cliques)}")


