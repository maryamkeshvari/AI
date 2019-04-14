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
print(train.isna().head())
print(test.isna().head())
print("*****Train_Set*****")
print(train.isna().sum())

print("*****Test_Set*****")
print(test.isna().sum())
print("______")
train.fillna(train.mean(),inplace=True)
print(train.isna().sum())
test.fillna(test.mean(),inplace=True)
print(test.isna().sum())
print(train.info())
train=train.drop(['Name','Ticket','Cabin','Embarked'],axis=1)
print(train.columns.values)
test=test.drop(['Name','Ticket','Cabin','Embarked'],axis=1)
print(test.columns.values)



labelEncoder=LabelEncoder()
labelEncoder.fit(train['Sex'])
labelEncoder.fit(test['Sex'])
train['Sex']=labelEncoder.transform(train['Sex'])
test['Sex']=labelEncoder.transform(test['Sex'])
print(train.info())
X=np.array(train.drop(['Survived'],1).astype(float))
y=np.array(train['Survived'])
#print(X,y)
kmeans=KMeans(n_clusters=2)
kmeans.fit(X)
