#!/usr/bin/python3

"""helpers.py Contains helper functions for lab 2

For the ID2222 Data Mining course at KTH Royal Institute of Technology"""

__author__ = "Xenia Ioannidou and Bas Straathof"


import pandas as pd
import csv


def load_dataset(file: str)-> pd.DataFrame:
    df = pd.read_csv(file, header=None, sep='\s\s+|,', engine='python')
    return df

