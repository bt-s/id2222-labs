#!/usr/bin/python3

"""helpers.py Contains helper functions for lab 1

For the ID2222 Data Mining course at KTH Royal Institute of Technology"""

__author__ = "Xenia Ioannidou and Bas Straathof"

import pandas as pd
import numpy as np


def load_dataset(file_name: str) -> pd.DataFrame:
    """Loads a data set from a CSV file and returns a Pandas DataFrame"""
    df = pd.read_csv(file_name)

    return df


def compare_sets(S: np.ndarray, d1: int, d2: int) -> float:
    """Compare the Jaccard similarity between two documents

    Args:
        S: The signature matrix of shape (n_shingles, n_documents)
        d1: ID of document 1
        d2: ID of document 2

    Returns:
        The approximated Jaccard similarity between d1 and d2
    """
    return np.mean(S[:, d1] == S[:, d2])

