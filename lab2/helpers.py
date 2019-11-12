import pandas as pd
import csv


def load_dataset(file: str)-> pd.DataFrame:
    df = pd.read_csv(file, header=None, sep='\s\s+|,', engine='python')
    return df

