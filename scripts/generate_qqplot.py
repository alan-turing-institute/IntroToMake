#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Takes a single-column data file and creates a QQ-plot of the values.

Based on: 
http://scientificpythonsnippets.com/index.php/distributions/6-q-q-plot-in-python-to-test-if-data-is-normally-distributed

Author: Gertjan van den Burg

"""

import argparse
import numpy as np
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

    # create QQ-plot
    x.sort()
    norm = np.random.normal(0, 2, len(x))
    norm.sort()
    plt.plot(norm, x, "o")
    z = np.polyfit(norm, x, 1)
    p = np.poly1d(z)
    plt.plot(norm, p(norm), "k--", linewidth=2)
    plt.xlabel("theoretical quantiles")
    plt.ylabel("empirical quantiles")
    plt.tight_layout()

    # write output
    if args.output:
        plt.savefig(args.output)
    else:
        plt.show()


if __name__ == "__main__":
    main()
