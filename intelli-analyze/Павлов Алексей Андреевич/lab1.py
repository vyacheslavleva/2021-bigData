from itertools import count

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('./flavors_of_cacao.csv', header=0)
rating = data['Rating']
data['Cocoa Percent'] = data['Cocoa Percent'].replace('%', '', regex=True)
cocoaColumn = data.sort_values(by='Cocoa Percent')['Cocoa Percent'].unique()
cocoaGroup = data.groupby('Cocoa Percent')['Rating']

# Первый пункт

refGroup = data[['REF', 'Rating']]
i = 0
while i <= len(str(refGroup['REF'].max())):
    i += 1
    refGroup.loc[refGroup['REF'] > 9, 'REF'] //= 10
refGroup = refGroup.groupby("REF")[['REF', 'Rating']]

# Второй пункт

plt.figure(figsize=(15, 7))
сolumn = refGroup.groups.keys()
dispers = np.empty(9)

dispers[...] = rating.var()
plt.subplot(2, 2, 1)
plt.plot(сolumn, refGroup.var().fillna(0)['Rating'], label='Дисперсия Rating')
plt.plot(сolumn, dispers, label='Общая дисперсия')
plt.title("Дисперсия")
plt.legend(fontsize=10)

dispers[...] = rating.mean()
plt.subplot(2, 2, 2)
plt.plot(сolumn, refGroup.mean()['Rating'], label='Среднее Rating')
plt.plot(сolumn, dispers, label='Общее среднее')
plt.title("Среднее")
plt.legend(fontsize=10)

dispers[...] = rating.median()
plt.subplot(2, 2, 3)
plt.plot(сolumn, refGroup.median()['Rating'], label='Медианное Rating')
plt.plot(сolumn, dispers, label='Общее Медианное')
plt.title("Медианное")
plt.legend(fontsize=10)

dispers[...] = rating.std()
plt.subplot(2, 2, 4)
plt.plot(сolumn, refGroup.std()['Rating'], label='СКО Rating')
plt.plot(сolumn, dispers, label='Общее СКО')
plt.title("СКО")
plt.legend(fontsize=10)

plt.show()

# Третий пункт

plt.figure(figsize=(15, 7))
dispers = np.empty(len(cocoaColumn))

dispers[...] = cocoaGroup.var().fillna(0)
plt.subplot(2, 1, 1)
plt.plot(cocoaColumn, dispers, label='Дисперсия')
dispers[...] = rating.var()
plt.plot(cocoaColumn, dispers, label='Общая дисперсия')
plt.title("Дисперсия")
plt.legend(fontsize=10)

dispers[...] = cocoaGroup.max() - cocoaGroup.min()
plt.subplot(2, 1, 2)
plt.plot(cocoaColumn, dispers, label='Размах')
dispers[...] = rating.max() - rating.min()
plt.plot(cocoaColumn, dispers, label='Общий размах')
plt.title("Размах")
plt.legend(fontsize=10)

plt.show()
