import pandas as pd

dataFile = 'path'

data = pd.read_csv(dataFile, sep=';', header=0, names=['user', 'isbn', 'rating'])