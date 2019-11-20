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


class Triest():
    def __init__(self, Sigma: Graph, M: int):
        """Class constructor

            Args:
                Sigma:
                M:
        """
        self.Sigma = Sigma
        self.M = M

        # Initialize the global triangle counter
        self.tau = 0

        # Initialize the reservoir graph
        self.S = nx.Graph()

    def triest_base(self) -> Graph:
        # Get a list of the edges
        Sigma_e = list(self.Sigma.edges)

        # Initialize the list of reservoir edges
        S_e = []

        for t, new_edge in enumerate(Sigma_e):
            if t < self.M:
                S_e.append(new_edge)
                self.S.add_edge(*new_edge)
                tau = self.update_counters(1, new_edge)
            else:
                j = np.random.randint(t)

                if j < self.M:
                    old_edge = random.choice(S_e)
                    S_e.remove(old_edge)
                    self.S.remove_edge(*old_edge)
                    tau = self.update_counters(-1, old_edge)

                    S_e.append(new_edge)
                    self.S.add_edge(*new_edge)
                    tau = self.update_counters(1, new_edge)

        return self.S, self.tau

    def update_counters(self, val, edge):
        n_u = set(self.S.neighbors(edge[0]))
        n_v = set(self.S.neighbors(edge[1]))
        n_uv = n_u.intersection(n_v)

        for n in range(len(n_uv)):
            self.tau += val

        return self.tau

