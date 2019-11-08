#!/usr/bin/python3

"""shingles.py Contains the Shingles class

For the ID2222 Data Mining course at KTH Royal Institute of Technology"""

__author__ = "Xenia Ioannidou and Bas Straathof"


import pandas as pd
import random
from typing import Set

random.seed(42)


class Shingles():
    def __init__(self, k=10):
        """Class constructor

        Attributes:
            k (int): Size of shingles
        """
        self.k = k

    def create_shingles(self, df_strings: pd.DataFrame, print_shingles:
            bool=False, print_hashed_shingles: bool=False) -> pd.DataFrame:
        """Creates a new dataframe of hashed shingles

        Args:
            df_strings: Data frame with n = # rows == # documents of
                        shape (n, 1)
            print_shingles: Whether to print the shingles per document
            print_hashed_shingles: Whether to print the shingles per document

        Returns:
            df_shingles: Data frame with n = # rows == # documents of
                         shape (n, 1)
        """
        all_shingles_set = set()

        if print_shingles:
            print("SHINGLES:\n")

        df_shingles = pd.DataFrame(columns=["documents"])
        for i, row in df_strings.iterrows():
            shingles = [row["documents"][i:i+self.k] for i in range(len(
                row["documents"])-self.k+1)]

            if print_shingles:
                print(f"Document {i}: {shingles}\n")

            # Use set() to remove duplicates
            df_shingles.loc[i] = {"documents" : set(shingles)}
            all_shingles_set = all_shingles_set.union(shingles)


        # Create a hash function
        all_shingles_dict = {}
        hashes = random.sample(range(1, 2**32-1), len(all_shingles_set))
        for i, shingle in enumerate(sorted(list(all_shingles_set))):
            all_shingles_dict[shingle] = hashes[i]

        if print_hashed_shingles:
            print("HASHED SHINGLES:\n")

        # Apply the hash function to the data frame
        for i, row in df_shingles.iterrows():
            hashed_shingles = []
            for j, shingle in enumerate(row["documents"]):
                hashed_shingles.append(all_shingles_dict[shingle])

            if print_hashed_shingles:
                print(f"Document {i}: {hashed_shingles}\n")

            row["documents"] = sorted(hashed_shingles)

        return df_shingles

    def compare_sets(self, d1: Set, d2: Set, print_sim: bool=False) -> float:
        """Compare the Jaccard similarity between two documents

        Args:
            d1: Set of hashed shingles (ints) of document 1
            d2: Set of hashed shingles (ints) of document 2
            print_sim: Whether to print the result

        Returns:
            The Jaccard similarity between d1 and d2

        Note: Jaccard similarity = intersection / union
        """
        sim = len(d1.intersection(d2)) / len(d1.union(d2))

        if print_sim:
            print(f"The approximated Jaccard similarity between the documents is: "
                    f"{sim}.")

        return len(d1.intersection(d2)) / len(d1.union(d2))


