import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

data = pd.read_csv(r'C:\Users\Junling\github\NHL-SportsPredictor\2019-skater-stats.csv')

print(data.head())
