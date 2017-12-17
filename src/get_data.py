# get_data.py
# Nazli Ozum Kafaee, Dec 2017
#
# This script takes data from url and writes it to a .csv file.
# This script takes a url and a filename as the variable arguments.
#
# Dependencies: argparse, pandas
#
# Usage: python get_data.py url target_file


# Import libraries
import pandas as pd
import argparse

# Read in command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('target_file')
args = parser.parse_args()

# Get the data from url and create a frame
wine = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data", header = None)

# Write the data frame to a csv file
wine.to_csv(args.target_file, encoding='utf-8', index=False, header=False)
