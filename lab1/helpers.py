#!/usr/bin/python3

"""helpers.py Contains helper functions for lab 1

For the ID2222 Data Mining course at KTH Royal Institute of Technology"""

__author__ = "Xenia Ioannidou and Bas Straathof"

import pandas as pd


def load_dataset(file_name: str) -> pd.DataFrame:
    """Loads a data set from a CSV file and returns a Pandas DataFrame"""
    df = pd.read_csv(file_name)

    return df


