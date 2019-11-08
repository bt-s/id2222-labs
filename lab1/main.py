#!/usr/bin/python3

"""main.py Contains all experiments for lab 1

For the ID2222 Data Mining course at KTH Royal Institute of Technology"""

__author__ = "Xenia Ioannidou and Bas Straathof"


import pandas as pd
from argparse import ArgumentParser, Namespace
from sys import argv

from helpers import load_dataset, compare_sets
from shingles import Shingles
from min_hashing import MinHash
from lsh import LSH


def parse_args():
    """Parses CL arguments"""
    parser = ArgumentParser()

    parser.add_argument("-d", "--dataset", type=str, default="toy_dataset.csv")
    parser.add_argument("-t", "--task", type=str, default="shingles",
            help="The task that should be carried out: shingles, minhash or "
            "lsh.")

    return parser.parse_args(argv[1:])


def main(args: Namespace):
    """Main function for lab 1

    Args:
        args: CL arguments
    """
    X = load_dataset(args.dataset)

    if args.task == "shingles":
        PRINT_SIM = True

        # Define the Shingles object
        obj = Shingles()

        # Create a shingles dataframe based on the data
        df_shingles = obj.create_shingles(X, print_shingles=True,
                print_hashed_shingles=True)

        # Create sets of shingles for the first two documents
        set_d1 = set(df_shingles.iloc[8].to_list()[0])
        set_d2 = set(df_shingles.iloc[9].to_list()[0])

        # Compare the hash-shingled documents using Jaccard similarity
        if PRINT_SIM:
            print("Documents:\n - woman, man, child, sister, brother, pants\n"
            "- woman, man, child, sister, brother, lecture hall\n")

        obj.compare_sets(set_d1, set_d2, print_sim=PRINT_SIM)


    if args.task == "minhash":
        # Define the MinHash object
        obj = MinHash()

        # Create the characteristic matrix
        M = obj.create_shingles(X)

        # Create the signature  matrix
        S = obj.create_signatures(M, k=1000)
        print(f"The approximated Jaccard similarity between document d1 and d2 is: "
                f"{compare_sets(S, 0, 1)}")

    if args.task == "lsh":
        # Define the MinHash object
        mh = MinHash()

        # Create the characteristic matrix
        M = mh.create_shingles(X)

        # Create the signature  matrix
        S = mh.create_signatures(M, k=1000)

        # Define the LSH object
        lsh = LSH(S)

        #print(f"The approximated Jaccard similarity between document d1 and d2 is: "
                #f"{compare_sets(S, 0, 1)}")

        pairs = lsh.find_candidate_pairs(S, bands=50)
        pairs = lsh.compare_pairs(S, pairs)
        print(pairs)

if __name__ == "__main__":
    main(parse_args())

