## Objectives

The aim of this project is to practice best practices in data science workflows as well as some newly-acquired supervised machine learning techniques. 

In this project, I implement the k-nearest neighbours algorithm and the decision tree algorithm on the [Wine Data Set](https://archive.ics.uci.edu/ml/datasets/wine). In the end, I get the accuracy score of both algorithms when predicting the type of wine for a new  input. 

I present the accuracy scores as percentages. I am interested in whether there will be a dramatic difference in the accuracy scores of these algorithms and if there is, which one will be higher.


## Data

The data used in this project is from [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php). It consists of 178 observations, 13 attributes and 3 classes of wine.

The data is also available in current repository as [wine_data.csv](data/wine_data.csv).


## System Requirements

* Python 3.6 and packages:
	* scikit-learn==0.18.1
	* pandas==0.20.1
	* numpy==1.12.1
	* argparse==1.4.0
	* matplotlib==2.0.2

## Dependency Diagram

![](docs/dependency_diagram.png)


## Reproducing the Analysis

Clone this repository or download it. Then, `cd` to the project directory on your computer. The project directory already has the intermediate files of the analysis that has been run before. In order to clean the analysis and re-run it, first, run `make clean`.

You can use two options to run the analysis. The directions for both are explained as follows:

__Using conda environment:__

Run the command below.

```
conda env create -f environment.yml
```

This will create the python environment required for the analysis. Then run the command below to carry out the analysis from top to bottom.

```
make all
```

__Using docker image:__

If you have Docker installed on your computer, you can run the command below that will tell automatically download/pull the Docker image required for this analysis. Don't forget to modify the `VOLUME_ON_YOUR_COMPUTER` part with the appropriate path to the project directory on your computer.

```
docker run --rm -it -v VOLUME_ON_YOUR_COMPUTER:/home/wine_classification nazliozum/wine_classification /bin/bash
```

Now, your prompt should change to look something like this:

```
root@1fc309a08883:/#
```

Then `cd` into the `/home/wine_classification` directory and then run `make all`.

Now, the whole analysis will run from top to bottom.

You can use the command `exit` to exit the container and go back to your regular Shell.


## Author

Nazli Ozum Kafaee