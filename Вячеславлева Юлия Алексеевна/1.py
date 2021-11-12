import numpy as np
import pandas as pd

rng = np.random.default_rng()
df1 = pd.DataFrame(rng.integers(-1000, 5000, size=(9000, 4)))
df2 = pd.DataFrame(rng.random((9000, 3)))

data = pd.concat([df1, df2], axis=1)
data.columns = [x for x in range(7)]
#data.to_csv('vyacheslavleva', sep='\t')

df = pd.read_csv('vavilova', sep='\t')

print(df.head())

for i in range(100):
    df.at[np.random.randint(0, 9000), 0] = None
    df.at[np.random.randint(0, 9000), 0] = None
    df.at[np.random.randint(0, 9000), 0] = None

df.to_csv('vavilova_1', sep='\t')
print(df.head())