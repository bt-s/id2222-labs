#!/usr/bin/python3.7

"""apriori.py Contains an implementation of the Apriori algorithm

For the ID2222 Data Mining course at KTH Royal Institute of Technology"""

__author__ = "Xenia Ioannidou and Bas Straathof"


import numpy as np
import pandas as pd
import itertools
from typing import Dict


def apriori(df: pd.DataFrame, s: int, K:int) -> Dict:
    """Finds frequent itemsets with support at least s

    Args:
      df: Input data frame
      s: Support
      K: k-itemsets

    Returns:
        f_item_sets: All frequent item_sets and their support
    """
    # Store all frequent itemsets and their support
    f_item_sets = {}

    # A-Priori pass for each of 1 up to K-itemsets
    for k in range(0, K+1):
        # Create a dictionary for counting k-itemsets
        counts = {}

        for i, row in df.iterrows():
            # Turn the pandas.Series into a list of integers
            row = list(map(int, row.tolist()[0].split()))

            if k == 0:
                Ck = list(itertools.combinations(row, 1))
            else:
                # Turn the list of integers into a list of tuples
                row = list(itertools.combinations(row, k))

                # Find candidate k-1-itemsets
                Ck_min_1 = []
                for k_item in row:
                    # Note Lk here is Lk-1
                    if Lk[k_item] != 0:
                        Ck_min_1.append(k_item)

                # Turn Ck_min_1 into a set of frequent singletons
                f_singletons = set([x for l in Ck_min_1 for x in l])

                # Obtain all candidate frequent k-itemsets
                Ck = list(itertools.combinations(f_singletons, k+1))

            # Loop over the candidate items and count them
            for item in Ck:
                if item not in counts.keys():
                    counts[item] = 1
                else:
                    counts[item] += 1

            if not k == 0:
                # Only keep the items in the basket that are candidate
                # f_singletons
                df.loc[i] = ' '.join(list(map(str, f_singletons)))

        # Determine which items as frequent
        Lk = {}
        for key, v in counts.items():
            if v >= s:
                # Create a unique hash for the frequent itemset
                Lk[key] = hash(key)

                # Store the frequent itemset and its support
                f_item_sets[key] = v
            else:
                Lk[key] = 0

        if Lk == {}:
            print(f"There are at most {k}-itemsets.\n")
            break

    return f_item_sets

