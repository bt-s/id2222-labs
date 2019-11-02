#!/usr/bin/python3

"""main.py Contains all experiments for lab 1

For the ID2222 Data Mining course at KTH Royal Institute of Technology"""

__author__ = "Xenia Ioannidou and Bas Straathof"


import pandas as pd

from helpers import load_dataset
from shingles import Shingles
from min_hashing import MinHash

# To use the very simple toy data set
TOY_TOY_DATASET = False

SHINGLES = False
MINHASH = True

if TOY_TOY_DATASET:
    X = load_dataset("toy_toy_dataset.csv")
else:
    X = load_dataset("toy_dataset.csv")

# Sanity-check that X is a pandas DataFrame
assert type(X) == pd.DataFrame


if SHINGLES:
    # Define the Shingles object
    obj = Shingles()

    # Create a shingles dataframe based on the data
    df_shingles = obj.create_shingles(X)

    # Create sets of shingles for the first two documents
    set_d1 = set(df_shingles.iloc[0].to_list()[0])
    set_d2 = set(df_shingles.iloc[1].to_list()[0])

    # Compare the hash-shingled documents using Jaccard similarity
    obj.compare_sets(set_d1, set_d1)


if MINHASH:
    # Define the MinHash object
    obj = MinHash()

    # Create the characteristic matrix
    M = obj.create_shingles(X)

    # Create the signature  matrix
    S = obj.create_signatures(M, k=1000)
    print(f"The approximated Jaccard similarity between document d1 and d2 is: "
            f"{obj.compare_sets(S, 0, 1)}")

