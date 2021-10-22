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
df=pd.read_csv('suslov', sep='\t', header=0, index_col=0)#,dtype={0: np.int64, 1: np.int64, 2:np.int64, 3:np.int64, 4: np.float64, 5:np.float64, 6:np.float64})
df.columns=[x for x in range (7)]
#a= (sum(df[4]))+(sum(df[5]))+(sum(df[6]))/(len(df[4])+len(df[5])+len(df[6]))
a=sum(df[4:])/len(df[4:])
print (a)
#print(df[4:].mean)
min_int_value=int(sum([df[0].mean(), df[1].mean(),df[2].mean(),df[3].mean()]))
print (min_int_value)
for i in range(100):
	df.at[np.random.randint(0,9000), 0] /= 2
	df.at[np.random.randint(0,9000), 1] = None
	df.at[np.random.randint(0,9000), 5] = -9999999
	df.at[np.random.randint(0,9000), 3] = None
from math import factorial
#print(factorial(min_int_value))
df.to_csv('suslov',sep='\t')
def map_data(df):
	#df.isnull
	#df.ge
	#df.dtypes
	#df.empty
	#or df[0:3].dtypes()!=float or df[4:6].abs().ge(1),
	#clear_data=pd.DataFrame(list(filter(df.isnull(), df)))
	clear_data = (df.isnull(), df)
	return clear_data

print (map_data(df))
map_data(df).to_csv('suslov_isnull', sep='\t')
