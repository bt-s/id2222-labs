#!/usr/bin/python3.7

"""resevoir_sampling.py Implementation of the resevoir sampling algorithm
                        in its most simple form

For the ID2222 Data Mining course at KTH Royal Institute of Technology"""

__author__ = "Xenia Ioannidou and Bas Straathof"



from networkx.classes.graph import Graph
import networkx as nx
import numpy as np
import random

from helpers import draw_graph


def reservoir_sampling(Sigma: Graph, M: int) -> Graph:
    # Get a list of the edges
    Sigma_e = list(Sigma.edges)

    # Initialize the list of edges
    S_e = []

    for t in range(M):
        S_e.append(Sigma_e[t])

    for t in range(M, len(Sigma_e)):
        j = np.random.randint(t)

        if j < M:
            S_e.remove(random.choice(S_e))
            S_e.append(Sigma_e[t])

    # Initialize the reservoir graph
    S = nx.Graph()
    S.add_edges_from(S_e)

    return S

