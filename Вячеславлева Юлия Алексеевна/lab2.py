import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('C:/Users/vja20/OneDrive/Документы/GitHub/2021-bigData/_lab-2/GoT/battles.csv', header=0)
print(data.head())

attacker = data.groupby(['attacker_king', 'year'], dropna=True)[['year']]
attacker.agg('count').to_csv('l2', sep=',')
print(attacker.agg('count'))
print(" ")
defender = data.groupby(['defender_king', 'year'], dropna=True)[['year']]
defender.agg('count').to_csv('l22', sep=',')
print(defender.agg('count'))
print(" ")

df1 = pd.read_csv('l2', header=0, sep=',', na_filter=True, names=['king', 'year', 'count'])
df2 = pd.read_csv('l22', header=0, sep=',', na_filter=True, names=['king', 'year', 'count'])
df3 = pd.concat([df1, df2], axis=0, ignore_index=True)
df3.to_csv('222', sep=',')
print(df3)
print(" ")
df4 = df3.groupby(['king', 'year'], dropna=True)[['count']]
df4.agg('sum').to_csv('exit', sep='\t')
df4 = pd.read_csv('exit', header=0, sep='\t', na_filter=True, names=['king', 'year', 'count'])
print(df4)

# make the data
np.random.seed(3)
x = df4['year']
y = df4['king']
# size and color:
sizes = df4['count']*8
colors = np.random.uniform(15, 80, len(x))
# plot
fig, ax = plt.subplots()
ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=200)
# zip joins x and y coordinates in pairs
for x1, y1, s1 in zip(x, y, sizes):
    label = round(s1/df4['count'].agg('sum'), 3)
    plt.annotate(label, # this is the text
                 (x1, y1), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0, 5), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

ax.set(xlim=(297, 301), xticks=np.arange(298, 301))
plt.show()