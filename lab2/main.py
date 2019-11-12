import os.path
from helpers import load_dataset
from argparse import ArgumentParser, Namespace
from sys import argv
from IPython.display import display, HTML


def parse_args():
    """Parses CL arguments"""
    parser = ArgumentParser()

    parser.add_argument("-d", "--dataset", type=str, default="./T10I4D100K.dat")
    parser.add_argument("-t", "--sub_problem", type=str, default="1",
            help="The task that should be carried out: sub_problem 1 or sub_p")

    return parser.parse_args(argv[1:])

def main(args: Namespace):

    try:
        df = load_dataset(args.dataset)
        display(df)
    except FileNotFoundError:
        print("File does not exist")


if __name__ == "__main__":
    main(parse_args())