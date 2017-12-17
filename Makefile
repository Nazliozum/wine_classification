# Driver script
# Nazli Ozum Kafaee, December 2017
# Completes knn and decision tree analysis from top to bottom (from raw data to rendering report)
#
# Usage: make all

# Run all analysis
all: results/accuracy_score_knn.txt results/accuracy_score_dtree.txt results/figures/tree.png docs/Report.html

# Get the data
data/wine_data.csv: src/get_data.py
	python $< $@

# Get the optimum k value
results/optimum_k.txt: data/wine_data.csv src/knn_cv.py
	python src/knn_cv.py $< $@

# Get the test accuracy score for knn
results/accuracy_score_knn.txt: data/wine_data.csv results/optimum_k.txt src/knn_testscore.py
	python src/knn_testscore.py $< results/optimum_k.txt $@

# Get the optimum tree depth
results/optimum_depth.txt: data/wine_data.csv src/dtree_cv.py
	python src/dtree_cv.py $< $@

# Get the test accuracy of decision tree
results/accuracy_score_dtree.txt: data/wine_data.csv results/optimum_depth.txt src/dtree_testscore.py
	python src/dtree_testscore.py $< results/optimum_depth.txt $@

# Convert tree.dot to tree.png
results/figures/tree.png: results/figures/tree.dot
	dot -Tpng $< -o $@

# Render the report to markdown document
docs/Report.html: src/Report.Rmd
	Rscript -e 'ezknitr::ezknit("src/Report.Rmd", out_dir = "docs")' $@

# Clean up intermediate files
clean:
	rm -f data/wine_data.csv
	rm -f results/*.txt
	rm -f results/figures/*.png
	rm -f results/figures/tree.dot
	rm -f docs/Report.md docs/Report.html
