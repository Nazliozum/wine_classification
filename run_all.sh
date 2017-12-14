# run_all.sh
# Nazli Ozum Kafaee, Dec 2017
#
# This driver script implements the knn and decision tree
# algorithm on the Wine Data Set. This script
# takes no arguments.
#
# Usage: bash run_all.sh

# Get the data
python src/get_data.py https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data data/wine_data.csv

# Get the optimum k value
python src/knn_cv.py data/wine_data.csv 7 results/optimum_k.txt

# Get the test accuracy score for knn
python src/knn_testscore.py data/wine_data.csv results/optimum_k.txt results/accuracy_score_knn.txt

# Get the optimum tree depth
python src/dtree_cv.py data/wine_data.csv 10 results/optimum_depth.txt

# Get the test accuracy of decision tree
python src/dtree_testscore.py data/wine_data.csv results/optimum_depth.txt results/accuracy_score_dtree.txt

# Convert tree.dot to tree.png
dot -Tpng results/tree.dot -o results/tree.png

# Render the final report
Rscript -e 'ezknitr::ezknit("src/Report.Rmd", out_dir = "docs")'
