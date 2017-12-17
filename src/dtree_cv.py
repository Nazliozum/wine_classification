# dtree_cv.py
# Nazli Ozum Kafaee, Dec 2017
#
# This script calculates the best level of depth to use in the
# decision tree model. Variable arguments are a data file
# and an integer indicating how many times to split the training data during
# cross validation.
#
# Dependencies: argparse, pandas, numpy, sklearn.tree, sklearn.model_selection
#
# Usage: python dtree_cv.py data_file target_file

# Import libraries
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import ShuffleSplit
import pandas as pd
import argparse

# Read in command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('data_file')
parser.add_argument('target_file')
args = parser.parse_args()

wine = pd.read_csv(args.data_file, header = None)

X = wine[wine.columns[1:]]
y = wine[wine.columns[0]]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)


# Create list that holds numbers for n_depth
depth = list(range(1,50))

# Create empty list that will hold cv scores
cv_scores = []

for n_depth in depth:
    mytree = DecisionTreeClassifier(max_depth = n_depth, random_state=0)
    cv = ShuffleSplit(n_splits = 10, test_size = 0.25, random_state = 0)
    scores = cross_val_score(mytree, X_train, y_train, cv = cv)
    cv_scores.append(scores.mean())

# Determine the best n_depth
score_depth_tuples = [i for i in zip(cv_scores, depth)]
optimum_depth = max(score_depth_tuples)[1]


# Write the optimal_k to a text file for future use
optimum_depth = str(optimum_depth)
file = open(args.target_file, 'w')
file.write(optimum_depth)
file.close()
