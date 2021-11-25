import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('C:/Users/vja20/OneDrive/Документы/GitHub/2021-bigData/_lab-2/GoT/battles.csv', header=0)

print(data.head())

#data.groupby('year')['name'].nunique().plot(kind='bar')
#plt.show()


name_a = data['attacker_king'].unique()
name_d = data['defender_king'].unique()
#name_a.fillna(value=0, inplace=True)
#name_d.fillna(value=0, inplace=True)
names = np.array([*name_a, *name_d])[np.array([*name_a, *name_d]) != 'nan']
names = list(set(names))
print(names)

attacker = data.groupby(['attacker_king', 'year'], dropna=True)[['year']]
attacker.agg('count').to_csv('l2', sep='\t')
print(attacker.agg('count'))
print(" ")
defener = data.groupby(['defender_king', 'year'], dropna=True)[['year']]
defener.agg('count').to_csv('l22', sep='\t')
print(defener.agg('count'))
print(" ")

df1 = pd.read_csv('l2', header=0, sep='\t')
df2 = pd.read_csv('l22', header=None, sep='\t', skiprows=[0])
#df3 = pd.concat([df1, df2], axis=0, ignore_index=True)
#df3.to_csv('222', sep='\t')
print(df1)
print(df1.index)
print(df1.columns)
print(df1.loc[1])

y = data.groupby('year')['name'].nunique()
#y = names
x = data['year'].unique()

k = []

print(len(x))
for i in range(1, len(x)):
    k.append((y.iat[i]-y.iat[i-1])/(x[i]-x[i-1]))
k_m = np.mean(k)

#plt.plot(x, y) #comment for test
#plt.show()

# make the data
np.random.seed(3)
x = df1['year']
y = df1['attacker_king']
# size and color:
sizes = df1['year.1']
colors = np.random.uniform(15, 80, len(x))

# plot
fig, ax = plt.subplots()

ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)

ax.set(xlim=(297, 301), xticks=np.arange(298, 301))

plt.show()