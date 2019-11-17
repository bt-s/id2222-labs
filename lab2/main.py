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

    parser.add_argument("-d", "--dataset", type=str, default="./toy.csv")
    parser.add_argument("-s", "--support", type=int, default=2)
    parser.add_argument("-c", "--confidence", type=float, default=0.5)
    parser.add_argument("-k", "--k", type=int, default=10)

    return parser.parse_args(argv[1:])


def main(args: Namespace):

    try:
        df = load_dataset(args.dataset)
        f_item_sets = apriori(df, args.support, args.k)
        print("The frequent item sets are:")
        print(f_item_sets)
        a_rules = association_rules(f_item_sets, args.confidence)
        print("\nThe association rules are:")
        for rule in a_rules.items():
            print(rule)

    except FileNotFoundError:
        print("File does not exist")


if __name__ == "__main__":
    main(parse_args())

