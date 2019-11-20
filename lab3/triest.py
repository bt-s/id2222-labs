#!/usr/bin/python3.7

"""resevoir_sampling.py Implementation of the resevoir sampling algorithm
                        in its most simple form

For the ID2222 Data Mining course at KTH Royal Institute of Technology"""

__author__ = "Xenia Ioannidou and Bas Straathof"



from networkx.classes.graph import Graph
import networkx as nx
import numpy as np
from typing import Tuple
import random


class Triest():
    def __init__(self, Sigma: Graph, M: int):
        """Class constructor

            Args:
                Sigma: The graph to be processed as a data stream
                M: The number of edges to be saved in the reservoir
        """
        self.Sigma = Sigma
        self.M = M

        # Initialize the global triangle counter
        self.tau = 0

        # Initialize the reservoir graph
        self.S = nx.Graph()

    def update_counter(self, val: int, edge: Tuple):
        """Update the global triangle counter

        Args:
            val: Determines the sign of the counter, thus either 1 or -1
            edge: The edge between the two nodes for which we want to compute
                  the neighborhood

        Updates:
            self.tau
        """
        # The neighborhood of node u
        n_u = set(self.S.neighbors(edge[0]))
        # The neighborhood of node v
        n_v = set(self.S.neighbors(edge[1]))
        # The intersection of the neighborhoods of nodes u and v
        n_uv = n_u.intersection(n_v)
        # For each common neighborhood, update tau
        for n in range(len(n_uv)):
            self.tau += val

    def triest_base(self) -> Tuple[Graph, float]:
        """The base algorithm for counting graph triangles as suggested in the
           Triest paper

        Returns:
            self.S: The graph representation of the reservoir at the last
                    time-step
            est_glob_triangles: The estimate of the global amount of triangles
                                in Sigma

        Note: We prefer to work with lists in parallel to the graphs, since
              otherwise the graph's edges would have to be converted to a list
              everytime that we want to select a random edge, which is a costly
              operation. We also continuously update the graph, since we want to
              keep track of the neighborhood of each node.
        """
        # Get a list of the edges
        Sigma_e = list(self.Sigma.edges)

        # Initialize the list of reservoir edges
        S_e = []

        for t, new_edge in enumerate(Sigma_e):
            if t < self.M:
                S_e.append(new_edge)
                self.S.add_edge(*new_edge)
                tau = self.update_counter(1, new_edge)
            else:
                # Sample a random integer in the range (0, t)
                j = np.random.randint(t)

                if j < self.M:
                    # Randomly choose an old edge for deletion
                    old_edge = random.choice(S_e)
                    S_e.remove(old_edge)
                    self.S.remove_edge(*old_edge)
                    tau = self.update_counter(-1, old_edge)

                    S_e.append(new_edge)
                    self.S.add_edge(*new_edge)
                    tau = self.update_counter(1, new_edge)

        # Compute the triest coeffecient
        X = max(1, (t*(t-1)*(t-2))/(self.M*(self.M-1)*(self.M-2)))

        # Estimate of global triangles in Sigma
        est_glob_triangles = self.tau*X

        return self.S, est_glob_triangles

