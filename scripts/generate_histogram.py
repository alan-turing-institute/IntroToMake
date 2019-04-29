#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Takes a single-column data file and creates a histogram of the values.

Author: Gertjan van den Burg

"""

import argparse
import matplotlib.pyplot as plt
import os


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="input file", required=True)
    parser.add_argument("-o", "--output", help="output file")
    return parser.parse_args()


def main():
    # parse cli arguments
    args = parse_args()

    # read the data
    if not os.path.exists(args.input):
        raise os.FileNotFoundError(args.input)
    with open(args.input, "r") as fid:
        x = [float(l.strip()) for l in fid]

    # create histogram
    plt.hist(x, bins="auto")
    plt.xlabel("rating")
    plt.ylabel("count")
    plt.tight_layout()

    # write output
    if args.output:
        plt.savefig(args.output)
    else:
        plt.show()


if __name__ == "__main__":
    main()
