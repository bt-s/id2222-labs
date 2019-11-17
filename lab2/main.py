#!/usr/bin/python3.7

"""main.py Contains all experiments for lab 2

For the ID2222 Data Mining course at KTH Royal Institute of Technology"""

__author__ = "Xenia Ioannidou and Bas Straathof"


from argparse import ArgumentParser, Namespace
from sys import argv

from helpers import load_dataset
from apriori import apriori
from association_rules import association_rules


def parse_args():
    """Parses CL arguments"""
    parser = ArgumentParser()

    parser.add_argument("-d", "--dataset", type=str, default="./T10I4D100K.dat")
    parser.add_argument("-s", "--support", type=int, default=1000)
    parser.add_argument("-c", "--confidence", type=float, default=0.5)
    parser.add_argument("-k", "--k", type=int, default=10)

    return parser.parse_args(argv[1:])


def main(args: Namespace):
    try:
        df = load_dataset(args.dataset)
        f_item_sets = apriori(df, args.support, args.k)
        lengths = {}
        for k,v in f_item_sets.items():
            if len(k) in lengths:
                lengths[len(k)] +=1
            else:
                lengths[len(k)] = 1
        print(f"The frequent itemsets are: {f_item_sets}\n")
        print(f"The distribution of frequent itemsets is: {lengths}.\n")
        a_rules = association_rules(f_item_sets, args.confidence)
        print("\nThe association rules are:")
        for rule in a_rules.items():
            print(rule)

        print(f"\nA total of {len(a_rules)} association rules was found.")

    except FileNotFoundError:
        print("File does not exist")


if __name__ == "__main__":
    main(parse_args())

