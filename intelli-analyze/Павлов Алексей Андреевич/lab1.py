import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('./flavors_of_cacao.csv', header=0)
rating = data['Rating']

# Первый пункт

refGroup = data[['REF', 'Rating']]
i = 0
while i <= len(str(refGroup['REF'].max())):
    i += 1
    refGroup.loc[refGroup['REF'] > 9, 'REF'] //= 10
refGroup = refGroup.groupby("REF")[['REF', 'Rating']]

# Второй пункт

plt.figure(figsize=(15, 7))
refColumn = refGroup.groups.keys()
dispers = np.empty(9)

dispers[...] = rating.var()
plt.subplot(2, 2, 1)
plt.plot(refColumn, refGroup.var().fillna(0)['Rating'], label='Дисперсия Rating')
plt.plot(refColumn, dispers, label='Общая дисперсия')
plt.title("Дисперсия")
plt.legend(fontsize=10)

dispers[...] = rating.mean()
plt.subplot(2, 2, 2)
plt.plot(refColumn, refGroup.mean()['Rating'], label='Среднее Rating')
plt.plot(refColumn, dispers, label='Общее среднее')
plt.title("Среднее")
plt.legend(fontsize=10)

dispers[...] = rating.median()
plt.subplot(2, 2, 3)
plt.plot(refColumn, refGroup.median()['Rating'], label='Медианное Rating')
plt.plot(refColumn, dispers, label='Общее Медианное')
plt.title("Медианное")
plt.legend(fontsize=10)

dispers[...] = rating.std()
plt.subplot(2, 2, 4)
plt.plot(refColumn, refGroup.std()['Rating'], label='СКО Rating')
plt.plot(refColumn, dispers, label='Общее СКО')
plt.title("СКО")
plt.legend(fontsize=10)

plt.show()
