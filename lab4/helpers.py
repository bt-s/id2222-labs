#!/usr/bin/python3

"""helpers.py Contains helper functions for lab 4

For the ID2222 Data Mining course at KTH Royal Institute of Technology"""

__author__ = "Xenia Ioannidou and Bas Straathof"


import networkx as nx
from networkx.classes.graph import Graph
from networkx.drawing.nx_pylab import draw_networkx
import matplotlib.pyplot as plt


def create_graph(f_name: str, n: int =2, sep: str =" ") -> Graph:
    """Creates a graph from a file

    Args:
        f_name: The filename/path
        n: The number of lines on the top of the file to skip
        sep: The value separator in the file

    Returns:
        G: The graph
    """
    data = open(f_name, "r")
    for i in range(n):
        next(data, None) # Delete a line in the input file

    # Define the graph type
    Graphtype = nx.Graph()

    # Define the graph
    G = nx.parse_edgelist(data, delimiter=sep, create_using=Graphtype,
            nodetype=int)

    return G


def draw_graph(G: Graph, labels: bool=True, save: bool=False,
        fname: str="test.pdf"):
    """Draw a graph structure

    Args:
        G: The graph to be drawn
        labels: Whether to draw the labels
        save: Whetehr to save the file
        fname: The path and name of the file to be saved
    """
    draw_networkx(G, with_labels=labels, node_color="lightblue")

    if save:
        plt.savefig(fname)
    else:
        plt.show()

    plt.close()


def get_graph_statistics(G):
    """Find the edges, nodes and triangles in a graph

    Args:
        G: The graph to be analyzed
    """
    print(f"The number of edges is: {len(G.edges)}")
    print(f"The number of nodes is: {len(G.nodes)}")
