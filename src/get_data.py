import pandas as pd
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('target_folder')

args = parser.parse_args()

wine = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data", header = None)

wine.to_csv(args.target_folder, encoding='utf-8', index=False, header=False)
