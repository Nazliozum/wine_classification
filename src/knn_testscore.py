# test_accuracy.py
# Nazli Ozum Kafaee, Dec 2017
#
# This script calculates the test accuracy for a specified
# data set from a .csv file. This script takes a data_file
# and a file giving the k-value and the target file to put the
# result as the variable arguments.
#
# Dependencies: argparse, pandas, numpy, sklearn.neighbors,
# sklearn.model_selection, sklearn.metrics
#
# Usage: python knn_testscore.py data_file k_file target_file


# import libraries
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# read in command line arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('data_file')
parser.add_argument('k_file')
parser.add_argument('target_file')
args = parser.parse_args()


# read in data
data = pd.read_csv(args.data_file, header = None)

X = data[data.columns[1:]]
y = data[data.columns[0]]

# The code below splits the data with 25% as test data.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state = 0)

# Get the value of the optimum k from the previous script
file = open(args.k_file, 'r')
k = int(file.read())
file.close()

# Predict for test data and measure accuracy
wine_knn = KNeighborsClassifier(n_neighbors = k)
wine_knn.fit(X_train, y_train)
predictions = wine_knn.predict(X_test)
accuracy = str(accuracy_score(predictions, y_test))

# Write accuracy rate to a text file
file = open(args.target_file, 'w')
file.write(accuracy)
file.close()
