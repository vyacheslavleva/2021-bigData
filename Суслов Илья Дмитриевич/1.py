import numpy as np
import pandas as pd

rng=np.random.default_rng()
#df1=pd.DataFrame(rng.integers(-1000, 5000, size=(9000,4)))
#df2=pd.DataFrame(rng.random((9000, 3)))

#data=pd.concat([df1, df2], axis=1)


#data.to_csv('suslov', sep='\t')

df=pd.read_csv('suslov', sep='\t')

df.columns=[0,1,2,3,4,5,6,7]
print (df.head())
for i in range(100):
	df.at[np.random.randint(0,9000), 0] = None
	df.at[np.random.randint(0,9000), 1] = None
	df.at[np.random.randint(0,9000), 2] = None
df.to_csv('suslov',sep='\t')
#Задача вернуть коверканный файл себе, считать его и сформулировать условия на проверку данных на уровне
#for rows in df:
#    for col in rows:
#       if col !=None:
#         result.append(col)