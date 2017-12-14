# knn_cv.py
# Nazli Ozum Kafaee, Dec 2017
#
# This script calculates the best k-value to use in the knn analysis and plots
# the level of accuracy vs k value.  Argument variables are a data file,
# an integer indicating how many times to split the training data during
# cross validation, and a target file to store the optimum k value.
#
# Dependencies: argparse, pandas, numpy, sklearn.neighbors,
# sklearn.model_selection, matplotlib.pyplot
#
# Usage: python knn_cv.py data_file n_splits target_file


# Import libraries
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import ShuffleSplit
import matplotlib.pyplot as plt
import argparse

# Read in command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('data_file')
parser.add_argument('target_file')
args = parser.parse_args()

# Read the data into a data frame
wine = pd.read_csv(args.data_file, header = None)

# Separate the data frame into features and labels
X = wine[wine.columns[1:]]
y = wine[wine.columns[0]]

# Separate the data into test and training data.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=0)

# Create odd list of k values
neighbors = list(range(1,50))

# Create empty list that will hold cv scores for each k value
cv_scores = []

# For loop that carries out 10-fold cross validation
for k in neighbors:
    wine_knn = KNeighborsClassifier(n_neighbors = k)
    cv = ShuffleSplit(n_splits = 7,
                                    test_size = 0.25, random_state = 0)
    scores = cross_val_score(wine_knn, X_train, y_train, cv=cv)
    cv_scores.append(scores.mean())

# Determine the best k
score_k_tuples = [i for i in zip(cv_scores, neighbors)]
optimum_k = max(score_k_tuples)[1]

# Write the optimal_k to a text file for future use
optimum_k = str(optimum_k)
file = open(args.target_file, 'w')
file.write(optimum_k)
file.close()

# Plot accuracy vs k value and save as the plot as png
plt.plot(neighbors, cv_scores)
plt.xlabel('Number of Neighbors (k)')
plt.ylabel('Training Accuracy')
plt.savefig("results/trainingaccuracy_vs_k.png")
