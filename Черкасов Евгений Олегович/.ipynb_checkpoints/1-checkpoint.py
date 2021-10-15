import numpy as np
import pandas as pd

def corrupt_the_file(file):
    frame = pd.read_csv(file,sep='\t')
    k = 0
    for i in range(int(len(frame)/100*5)):
        line = rng.integers(0,len(frame))
        col  = rng.integers(0,3)
        frame.iat[line,col] = rng.random() * 10000 - 5000
    frame.to_csv(file + '_corrupted', sep='\t',index=False)
    print(k)

#Создание и вывод моего набора данных
rng = np.random.default_rng()
df1 = pd.DataFrame(rng.integers(-1000,5000,size=(9000,4)))
df2 = pd.DataFrame(rng.random((9000,3)))

data = pd.concat([df1,df2],axis=1)
data.columns = [x for x in range(7)]
print(data.head())

# Запись и чтение моего набора
data.to_csv('cherkasov',sep='\t', index=False)
df = pd.read_csv('cherkasov',sep='\t')
print(df.head())

#Чтение чужого набора
r = pd.read_csv('fomin',sep='\t')
print(r.head())

#Порча чужого набора
corrupt_the_file('fomin')
d = pd.read_csv('fomin_corrupted',sep='\t')
print(d.head())