#!/usr/bin/python3.7

"""k_eigenvector.py Contains all functiosn for the k-eigenvector algorithm

For the ID2222 Data Mining course at KTH Royal Institute of Technology"""

__author__ = "Xenia Ioannidou and Bas Straathof"

import networkx as nx
from networkx.classes.graph import Graph
import numpy as np
import scipy
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def k_eigenvector(G: Graph, plot: bool=True, save: bool=True,
        gid: str=""):
    """Perform the k-eigenvector algorithm

    Args:
        G: The input graph
        plot: Whether to create plots
        save: Whether to save the plots
        gid: Identifier of the graph"""
    # Form the affinity matrix, which in this case boils down to the adjacency
    # matrix
    A = nx.adjacency_matrix(G).A

    # Form the diagonal matrix D^(-1/2)
    D = np.zeros(A.shape)
    np.fill_diagonal(D, 1/np.sqrt(A.sum(axis=1)))

    # Form the L matrix, where I - L == Laplacian matrix
    L = np.linalg.multi_dot([D, A, D])

    # Obtain all (sorted) eigenvalues and eigenvectors in L
    e_val, e_vec = np.linalg.eigh(L)

    # Identify the biggest spectral gap, which is a heuristic for the optimal k
    k = len(e_val) - np.argmax(np.ediff1d(e_val)) - 1

    # Keep only the k largest eigenvectors
    X = e_vec[:, -k:]

    # Normalize the matrix of k largest eigenvectors
    Y = X / X.sum(axis=0)[np.newaxis, :]

    # Peform the K-means algorihm on the k largest eigenvectors
    clusters = KMeans(n_clusters=k).fit(Y)

    # Get the labels belonging to the clusters
    labels = clusters.labels_

    # Generate various plots
    if plot:
        # Plot the sorted eigenvalues
        plt.title("Sorted Eigenvalues")
        plt.xlabel("Data Points")
        plt.ylabel("Values")
        plt.plot(e_val)

        if save:
            plt.savefig("imgs/" + gid + "_evs.pdf")
        else:
            plt.show()

        plt.close()

        # Plot the adjacency matrix
        plt.title("Adjacency Matrix")
        plt.xlabel("Data Points")
        plt.ylabel("Data Points")
        plt.imshow(A)

        if save:
            plt.savefig("imgs/" + gid + "_adjacency.pdf")
        else:
            plt.show()

        plt.close()

        # Plot the sorted Fiedler vector
        plt.title("Sorted Fiedler Vector")
        plt.xlabel("Data Points")
        plt.ylabel("Values")
        plt.plot(sorted(e_vec[:, 1]))

        if save:
            plt.savefig("imgs/" + gid + "_fiedler.pdf")
        else:
            plt.show()

        plt.close()

    return k, labels

