"""
---------------------------------------------------------------------
                            DATAQUEST

Data generation script for the "Introduction to Ensembles" blog post.
Author: Sebastian Flennerhag
---------------------------------------------------------------------
"""
from __future__ import print_function, division

import sys
import argparse
import numpy as np
import pandas as pd


USECOLS = ["cand_pty_affiliation",
           "cand_office_st",
           "cand_office",
           "cand_office_district",
           "cand_status",
           "rpt_tp",
           "transaction_pgi",
           "transaction_tp",
           "entity_tp",
           "state",
           "classification",
           "transaction_amt",
           "cycle"]

parser = argparse.ArgumentParser()
parser.add_argument('d', type=str,
                    choices=['y', 'n'],
                    help="Download original data from source")
parser.add_argument('-f', type=str,
                    help="filename of local source file")
parser.add_argument('-o', type=str, default='input.csv',
                    help="filename of output data (default: %(default)s)")

parser.add_argument('-n', type=int, default=100000,
                    help="Number of observations in output file (0=all, default: %(default)s)")
parser.add_argument('-s', type=int, default=222,
                    help="Seed to use for sampling output (0=None, default: %(default)s)")
parser.add_argument('-e', type=str, nargs='*',
                    default=['cand_office_district', 'transaction_pgi'],
                    choices=USECOLS,
                    help="Exclude features (default: %(default)s)")


if __name__ == '__main__':
    print(__doc__); sys.stdout.flush()
    args = parser.parse_args()

    # Drop excluded features
    usecols = [col for col in USECOLS if col not in args.e]

    # Load features
    if args.d == 'y':
        print("Downloading data ...", end=" "); sys.stdout.flush()
        f = ("https://media.githubusercontent.com/media/fivethirtyeight/"
             "data/master/science-giving/science_federal_giving.csv")
    else:
        print("Loading data from %s ..." % args.f, end=" "); sys.stdout.flush()
        f = args.f

    df = pd.read_csv(f, usecols=usecols, low_memory=False)

    print("done"); sys.stdout.flush()
    print("Formatting features ...", end=" "); sys.stdout.flush()

    # Drop NaNs
    df.dropna(inplace=True)
    if "cand_office_district" in df.columns:
        df.cand_office_district = df.cand_office_district.astype("object")

    if "cycle" in df.columns:
        df.loc[:, "cycle"] = df.loc[:, "cycle"].astype("object")

    # Filter out minor parties and negative contributions
    df = df.loc[
        df.cand_pty_affiliation.apply(lambda x: x in ["DEM", "REP"]), :]
    df = df.loc[df.transaction_amt > 0, :]

    print("done"); sys.stdout.flush()

    if args.n:
        print("Sampling ...", end=" "); sys.stdout.flush()
        if args.s:
            np.random.seed(args.s)

        idx = np.random.permutation(df.shape[0])
        df = df.iloc[idx, :]
        df.reset_index(drop=True, inplace=True)

        df = df.iloc[:args.n, :]
        print("done"); sys.stdout.flush()

    print("Writing to file ...", end=" "); sys.stdout.flush()
    df.to_csv(args.o, index=False)
    print("done"); sys.stdout.flush()

    print("Job complete."); sys.stdout.flush()
