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
# Usage: python dtree.py data_file depth_file target_file


# Import libraries
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
import graphviz
import matplotlib.pyplot as plt
from sklearn.tree import export_graphviz

import argparse

# Read in command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('data_file')
parser.add_argument('depth_file')
parser.add_argument('target_file')
args = parser.parse_args()

wine = pd.read_csv(args.data_file, header = None)

X = wine[wine.columns[1:]]
y = wine[wine.columns[0]]

X.feature_names = {'alcohol': 1, 'Malic acid': 2, 'Ash': 3,
'Alcalinity of ash': 4, 'Magnesium': 5, 'Total phenols': 6, 'Flavanoids': 7,
'Nonflavanoid phenols': 8, 'Proanthocyanins': 9, 'Color intensity': 10,
'Hue': 11, 'OD280/OD315 of diluted wines': 12, 'Proline': 13}

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# Get the value of the optimum depth from the previous script
file = open(args.depth_file, 'r')
depth = int(file.read())
file.close()

# Fit the model
mytree = DecisionTreeClassifier(max_depth = depth, random_state=0)
tree_model = mytree.fit(X_train, y_train)


# Make a visualization of the tree
export_graphviz(tree_model, out_file = "results/figures/tree.dot", class_names = ["wine 1", "wine 2", "wine 3"],
                impurity=False, filled=True)

# Make a visualization showing which features are more important
def plot_feature_importances_wine(model):
    n_features = X.shape[1]
    plt.barh(range(n_features), model.feature_importances_, align='center')
    plt.yticks(np.arange(n_features))
    plt.xlabel("Feature importance")
    plt.ylabel("Feature")

plot_feature_importances_wine(mytree)
plt.savefig("results/figures/feature_importances.png")

# Get accuracy score and write it to a text file
predictions = mytree.predict(X_test)
accuracyscore = str( accuracy_score(predictions, y_test) )

file = open(args.target_file, 'w')
file.write(accuracyscore)
file.close()
