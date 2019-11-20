#!/usr/bin/python3.7

"""main.py Contains all experiments for lab 2

For the ID2222 Data Mining course at KTH Royal Institute of Technology"""

__author__ = "Xenia Ioannidou and Bas Straathof"


from argparse import ArgumentParser, Namespace
from sys import argv
from typing import List
import csv

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


def get_transactions(fname: str) -> List[List[int]]:
    """Read transactions from file

    Args:
        fname: File name

    Returns:
        List of transactions, where each transaction is a list of integers
    """
    with open(fname, 'r') as f:
        return [[int(x) for x in line.split()] for line in f]


def main(args: Namespace):
    print(f"Dataset: {args.dataset}")
    print(f"Support: {args.support}")
    print(f"Confidence: {args.confidence}")
    print("-"*20, "\n")
    transactions = get_transactions(args.dataset)
    f_item_sets = apriori(transactions, args.support, args.k)
    lengths = {}
    for k,v in f_item_sets.items():
        if len(k) in lengths:
            lengths[len(k)] +=1
        else:
            lengths[len(k)] = 1

    if len(f_item_sets) <= 20:
        print(f"The frequent itemsets are:\n")
    else:
        print(f"The first 20 frequent itemsets are:\n")

    for i, (f_item_set, support) in enumerate(f_item_sets.items()):
        if i < 20:
            print(f_item_set, support)

    print(f"\nA total of {len(f_item_sets)} frequent itemsets was found.")
    print(f"The distribution of frequent itemsets is: {lengths}.\n")

    a_rules = association_rules(f_item_sets, args.confidence)

    if len(a_rules) <= 20:
        print(f"The association rules are:\n")
    else:
        print(f"The first 20 association rules are:\n")

    for i, rule in enumerate(a_rules.items()):
        if i < 20:
            print(rule)

    print(f"\nA total of {len(a_rules)} association rules was found.")


if __name__ == "__main__":
    main(parse_args())

