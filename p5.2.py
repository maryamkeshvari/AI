import pandas as pd
import matplotlib.pyplot as plt

data={'Name':['tom','ann','mary','allen'],'Family':['a','b','c','d'],'Age':[20,18,25,11]}
lst=["ok","hi","bye","good"]
df=pd.DataFrame(data,index=lst)
print(df)
#print(df['Name'])
#print(df.loc['ok'])
#print(df.iloc[1])
#print(df.iloc[1,2])
#print(df.iloc[:2])
#print(df.sum())
#print(df.mean())
#print(df.plot())
#print(df.plot.bar())
#print(df.plot.bar(stacked=True))
#print(df.plot.barh())
plt.show()
#df.to_csv("C:/Users/Labs/Desktop/AI/p1.csv")
df2=pd.read_csv("C:/Users/Labs/Desktop/AI/p1.csv",sep=",")
print(df2)
