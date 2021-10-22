import numpy as np
import pandas as pd

rng=np.random.default_rng()
#df1=pd.DataFrame(rng.integers(-1000, 5000, size=(9000,4)))
#df2=pd.DataFrame(rng.random((3000, 3)))
#
#data=pd.concat([df1, df2], axis=1)
#
#
#print (data.head())
#data.to_csv('suslov2', sep='\t')
df=pd.read_csv('suslov2', sep='\t', header=0, index_col=0)#,dtype={0: np.int64, 1: np.int64, 2:np.int64, 3:np.int64, 4: np.float64, 5:np.float64, 6:np.float64})
df.columns=[x for x in range (7)]
#a= (sum(df[4]))+(sum(df[5]))+(sum(df[6]))/(len(df[4])+len(df[5])+len(df[6]))
a=sum(df[4:])/len(df[4:])
print (a)