#!/usr/bin/python3

"""min_hashing.py Contains the MinHash class

For the ID2222 Data Mining course at KTH Royal Institute of Technology"""

__author__ = "Xenia Ioannidou and Bas Straathof"


import pandas as pd
import numpy as np
import random
from typing import Set

random.seed(42)


class MinHash():
    def __init__(self, k=3):
        """Class constructor

        Attributes:
            k (int): Size of shingles
        """
        self.k = k

    def create_shingles(self, df_strings: pd.DataFrame) -> np.ndarray:
        """Creates a characteristic matrix based on hashed shingles

        Args:
            df_strings: Data frame with n = # rows == # documents of
                        shape (n, 1)

        Returns:
            char_mat : characterstic matrix (2D array of shape (total
                       # shingles, # documents))
        """
        all_shingles_set = set()

        df_shingles = pd.DataFrame(columns=["documents"])
        for i, row in df_strings.iterrows():
            shingles = [row["documents"][i:i+self.k] for i in range(len(
                row["documents"])-self.k+1)]
            # Use set() to remove duplicates
            df_shingles.loc[i] = {"documents" : set(shingles)}
            all_shingles_set = all_shingles_set.union(shingles)

        # Create a hash function
        all_shingles_dict = {}
        for i, shingle in enumerate(sorted(list(all_shingles_set))):
            all_shingles_dict[shingle] = i

        # Initialize the characteristic matrix
        n_docs = df_strings.shape[0]
        n_shingles = len(all_shingles_set)
        char_mat = np.zeros((n_shingles, n_docs))

        # Apply the hash function to the data frame
        for i, row in df_shingles.iterrows():
            for j, shingle in enumerate(row["documents"]):
                char_mat[all_shingles_dict[shingle], i] = 1

        return char_mat

    def create_signatures(self, M: np.ndarray, k: int=100) -> np.ndarray:
        """Creates k signatures from the charactersitic matrix

        Args:
            M: The charactersistic matrix
            k: The number of hash functions/permutations

        Returns:
            S : The signature matrix
        """
        n_shingles = M.shape[0]
        S = np.zeros((k, M.shape[1]))

        for kk in range(k):
            # Create a permutation of length number of shingles
            permutation = np.arange(n_shingles)
            # Shuffly the permutation
            np.random.shuffle(permutation)

            # Create a hash table for the permation
            perm_dict = {}
            for i, p in enumerate(permutation):
                perm_dict[p] = i

            step, filled, is_finished = 0, 0, False
            while not is_finished:
                # Select a row from M based on the current step in the
                # permutation
                row = M[perm_dict[step], :]

                # Loop over all values in the row
                for ix, val in enumerate(row):
                    if int(val) == 1:
                        filled += 1
                        S[kk-1, ix] = step

                    # If a row in S is completely filled, we stop and break the
                    # loop
                    if filled == M.shape[1]:
                        is_finished = True
                        break

                step += 1

        return S

