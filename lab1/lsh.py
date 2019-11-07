#!/usr/bin/python3

"""lsh.py Contains the Locality-Sensitive Hashing class

For the ID2222 Data Mining course at KTH Royal Institute of Technology"""

__author__ = "Xenia Ioannidou and Bas Straathof"


import pandas as pd
import numpy as np
import random
from typing import List, Tuple
from collections import defaultdict
import itertools

from min_hashing import MinHash
from helpers import compare_sets

random.seed(42)


class LSH():
    def __init__(self, S: np.ndarray, t: float=0.2):
        """Class constructor

        Attributes:
            S: Signature matrix
            t: Similarity threshold
        """
        self.t = t

    def find_candidate_pairs(self, S: np.ndarray, bands: int, k: int = 250
            ) -> List[Tuple]:
        """Find candidate pairs in S based on t

        Args:
            S: Signature matrix
            bands: Number of bands
            k: Number of buckets

        Returns:
            candidate_pairs: List of candiate pairs
        """
        rows = len(S) / bands

        # Create a data structure for storing the hash tables
        LSHdict = [defaultdict(list) for b in range(bands)]

        # Check whether r is an integer
        if rows != int(rows):
            raise ValueError(f"This choise of b leads to rows={rows}, which is "
                    "not an integer.")
            exit()

        # Type-cast rows
        rows = int(rows)

        # Do the partitioning
        for b in range(bands):
            # Specify the band
            S_band = S[b*rows:(b+1)*rows, :]

            # Loop over the collums
            for c in range(S_band.shape[1]):
                # Hash the vectors to k buckets
                S_band_c = hash(tuple(S_band[:, c])) % k

                # Create the dictionary of hash values
                if S_band_c in LSHdict[b]:
                    # Append if multiple columns have the same hash value
                    LSHdict[b][S_band_c].append(c)
                else:
                    LSHdict[b][S_band_c] = [c]

        # Find all candidate pairs
        candidate_pairs = []
        for b in range(bands):
            for v in list(LSHdict[b]):
                if len(LSHdict[b][v]) > 1:
                    candidate_pairs += list(itertools.combinations(
                        LSHdict[b][v], 2))


        # Remove duplicates from candidate pairs
        candidate_pairs = list(set([tuple(sorted(t)) for t in
            candidate_pairs]))

        return candidate_pairs


    def compare_pairs(self, S: np.ndarray, pairs: List) -> List[Tuple]:
        """Find all candidate pairs in S

        Args:
            S: Signature matrix
            pairs: All candidate pairs

        Returns:
            similar_pairs: List of all the pairs more similar than the threshold
        """
        similar_pairs = []
        for pair in pairs:
            sim = compare_sets(S, pair[0], pair[1])
            if sim > self.t:
                similar_pairs.append(pair)

        return similar_pairs

