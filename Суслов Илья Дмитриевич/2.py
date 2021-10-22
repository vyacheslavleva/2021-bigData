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
df=pd.read_csv('suslov2', sep='\t')
df.columns=[0,1,2,3,4,5,6,7]
a= (sum(df[4]))+(sum(df[5]))+(sum(df[6]))/(len(df[4])+len(df[5])+len(df[6]))
print (a)