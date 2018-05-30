import numpy as np
import pandas as pd

dataset = pd.read_csv('denseRatingMatrix.csv',header=None)

print(dataset.shape)

userNonZero =  (dataset!=0).sum(1)

itemNonZero = (dataset[:]!=0).sum()

print(userNonZero.sum())