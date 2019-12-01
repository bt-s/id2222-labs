#!/usr/bin/python3.7

"""graph_sppectra.py

For the ID2222 Data Mining course at KTH Royal Institute of Technology"""

__author__ = "Xenia Ioannidou and Bas Straathof"

from sklearn import cluster
from sklearn.cluster import SpectralClustering, KMeans
import networkx as nx
from community import community_louvain
from networkx.classes.graph import Graph
from networkx.drawing.nx_pylab import draw_networkx
import matplotlib.pyplot as plt
import numpy as np
from helpers import *
import scipy as sp
import numpy.linalg
from sklearn import cluster
from collections import defaultdict
from matplotlib import cm
import seaborn as sns
import pandas as pd
from networkx.drawing.nx_pylab import draw_networkx
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.metrics.cluster import adjusted_rand_score
import os

np.seterr(divide='ignore', invalid='ignore')

class Graph_Spectra:

    def __init__(self, G):
        self.G = G

    def spectral_clustering(self):

        A = nx.adjacency_matrix(self.G).toarray()
        D = np.diag(np.sum(A, axis=1))
        D_inv = np.linalg.inv(np.sqrt(D))
        L = np.dot(np.dot(D_inv, A), D_inv)
        # print("shape of A: ", A.shape)
        # print("shape of D: ", D.shape)
        # L = D - A

        # Find eigenvalues and eigenvectors
        w_eigenvalues , v_eigenvectors = numpy.linalg.eigh(L)

        # Identify the biggest spectral gap, which is a heuristic for the optimal k
        k = len(w_eigenvalues) - np.argmax(np.ediff1d(w_eigenvalues)) - 1

        # Keep only the k largest eigenvectors
        X = v_eigenvectors[:, -k:]

        # Construct matrix Y by renormalizing X
        Y = np.divide(X, np.reshape(np.linalg.norm(X, axis=1), (X.shape[0], 1)))
        Y = Y[~np.isnan(Y).any(axis=1)]

        # Clustering
        clusters = KMeans(n_clusters=k).fit(Y)

        # Draw graph
        draw_networkx(self.G, with_labels=False, node_size=12, node_color=clusters.labels_)
        plt.show()

        # Get Fiedler Vector: The eigenvector corresponding to second smallest eigenvalue of L
        # v_eigenvectors.sort()
        fiedler = v_eigenvectors[:, 1]

        # Plot the sparsity pattern and sorted fiedler vector
        fig, ax = plt.subplots(figsize=(10, 8))
        plt.plot(np.sort(fiedler))
        # ax.set_ylim([0, 0.5])
        # ax.set_xlim([210, 230])
        plt.title('Sorted Fiedler Vector')
        plt.show()
