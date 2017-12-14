all: results/accuracy_score_knn.txt results/accuracy_score_dtree.txt results/tree.png

# Get the data
data/wine_data.csv: src/get_data2.py
	python src/get_data2.py data/wine_data.csv

# Get the optimum k value
results/optimum_k.txt: data/wine_data.csv src/knn_cv2.py
	python src/knn_cv2.py data/wine_data.csv results/optimum_k.txt

# Get the test accuracy score for knn
results/accuracy_score_knn.txt: data/wine_data.csv results/optimum_k.txt src/knn_testscore2.py
	python src/knn_testscore2.py data/wine_data.csv results/optimum_k.txt results/accuracy_score_knn.txt

# Get the optimum tree depth
results/optimum_depth.txt: data/wine_data.csv src/dtree_cv2.py
	python src/dtree_cv2.py data/wine_data.csv results/optimum_depth.txt

# Get the test accuracy of decision tree
results/accuracy_score_dtree.txt: data/wine_data.csv results/optimum_depth.txt src/dtree_testscore2.py
	python src/dtree_testscore2.py data/wine_data.csv results/optimum_depth.txt results/accuracy_score_dtree.txt

# Convert tree.dot to tree.png
results/tree.png: results/tree.dot
	dot -Tpng results/tree.dot -o results/tree.png

clean:
	rm -f data/wine_data.csv
	rm -f results/*.txt
	rm -f results/*.png
	rm -f docs/Report.html
	rm -f docs/Report.md
