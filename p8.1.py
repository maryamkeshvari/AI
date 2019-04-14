import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
train_url="http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
train=pd.read_csv(train_url)
test_url="http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/test.csv"
test=pd.read_csv(test_url)
print("*****Train_Set*****")
print(train.head())
print("\n")
print("*****Test_Set*****")
print(test.head())
print("*****Train_Set*****")
print(train.describe())
print("\n")
print("*****Test_Set*****")
print(test.describe())
print(train.columns.values)