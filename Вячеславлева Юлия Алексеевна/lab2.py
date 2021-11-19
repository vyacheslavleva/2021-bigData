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

year = []
#for age in data['year'].unique():
    #for name in names:
        #if data['attacker_king'] == names:
            #year[name] += 1

print(year)

y = data.groupby('year')['name'].nunique()
#y = names
x = data['year'].unique()

k = []

print(len(x))
for i in range(1, len(x)):
    k.append((y.iat[i]-y.iat[i-1])/(x[i]-x[i-1]))
k_m = np.mean(k)

plt.plot(x, y) #comment for test
#plt.show()

# make the data
np.random.seed(3)
x = 4 + np.random.normal(0, 2, 24)
y = 4 + np.random.normal(0, 2, len(x))
# size and color:
sizes = np.random.uniform(15, 80, len(x))
colors = np.random.uniform(15, 80, len(x))

# plot
fig, ax = plt.subplots()

ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()