import pandas as pd
import numpy as np
data = pd.read_csv('D:/python/BlackFriday.csv')
#print(len(np.unique(data['Age'])))
print(data[data['Gender'] == 'M'].sum())
