import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('../_lab-2/GoT/battles.csv',header=0)
print(data.head())
def func(data):
    data.loc[data['defender_1'] == 'Tully'].groupby(['year'])['battle_number'].nunique()
    
    return void

data.map(func,data)
data.plot(kind = 'bar')

plt.show()



