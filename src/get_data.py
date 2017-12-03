import pandas as pd

wine = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data", header = None)

wine.to_csv("data/wine_data.csv", encoding='utf-8', index=False, header=False)
