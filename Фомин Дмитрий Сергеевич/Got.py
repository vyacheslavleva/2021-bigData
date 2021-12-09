import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np

data = pd.read_csv('../_lab-2/GoT/battles.csv',header=0)
print(data.head())

pd.options.display.max_columns = 20

defenders = data['defender_1'].dropna().unique()    
print(defenders)
dataCollector=pd.DataFrame(data=None)

for i in defenders:
    y=data.loc[data['defender_1'] == i].groupby('year')['battle_number'].nunique(dropna=True)
    dataCollector=pd.concat([dataCollector,y],axis=1)
dataCollector.columns = defenders
graph = dataCollector.plot(kind = 'bar',stacked=True, colormap='Paired')
for i in range(data['defender_1'].dropna().nunique()):           
    graph.bar_label(graph.containers[i],label_type='center')

plt.show()



