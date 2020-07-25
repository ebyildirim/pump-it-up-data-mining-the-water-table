import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import VarianceThreshold

pd=pd.read_csv("train_label.csv")
constant_filter = VarianceThreshold(threshold=0.05)
constant_filter.fit(pd)
len(pd.columns[constant_filter.get_support()])


constant_columns = [column for column in pd.columns
                    if column not in pd.columns[constant_filter.get_support()]]

pd.drop(labels=constant_columns, axis=1, inplace=True)
print(constant_columns)
pd.to_csv("train_label_p.csv",index=False)
