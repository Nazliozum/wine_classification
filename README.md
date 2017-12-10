## Objectives

The aim of this project is to practice best practices in data science workflows as well as some newly-acquired supervised machine learning techniques. 

In this project, I implement the k-nearest neighbours algorithm and the decision tree algorithm on the [Wine Data Set](https://archive.ics.uci.edu/ml/datasets/wine). In the end, I get the accuracy score of both algorithms when predicting the type of wine for a new  input. 

I present the accuracy scores as percentages. I am interested in whether there will be a dramatic difference in the accuracy scores of these algorithms and if there is, which one will be higher.


## Data

The data used in this project is from [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php). It consists of 178 observations, 13 attributes and 3 classes of wine.

The data is also available in current repository as [wine_data.csv](data/wine_data.csv).


## System Requirements

* Python 3.6 and packages:
	* sklearn
	* pandas
	* numpy
	* argparse
	* matplotlib 

## Dependency Diagram

![](docs/dependency_diagram.png)


## Reproducing the Analysis

1) Download the `src` folder of this directory to your project directory on your local machine.

2) Set directory to your project folder on your local machine using the command line.

3) Run the following command on the command line to download the data.

```
python src/get_data.py https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data data/wine_data.csv
```

Run the following commands in order to reproduce the analysis.

4)

```
python src/knn_cv.py data/wine_data.csv 7 results/optimum_k.txt
```

5)

```
python src/knn_testscore.py data/wine_data.csv results/optimum_k.txt results/accuracy_score_knn.txt
```

6)

```
python src/dtree_cv.py data/wine_data.csv 10 results/optimum_depth.txt
```

7)

```
python src/dtree_testscore.py data/wine_data.csv results/optimum_depth.txt results/accuracy_score_dtree.txt
```

8)

```
dot -Tpng results/tree.dot -o results/tree.png
```

## Author

Nazli Ozum Kafaee