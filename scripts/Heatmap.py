import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  

data = np.random.randint(low=1, high=100, size=(10, 10))  
print(data)

sns.heatmap(data=data)
plt.show()

#color map
sns.heatmap(data=data,cmap="GnBu")
plt.show()

#Line colour and linewidth
sns.heatmap(data=data,linecolor="black",linewidth=2)
plt.show()

#Annot
sns.heatmap(data=data,annot=True)
plt.show()

#cbar
sns.heatmap(data=data,cbar=False)
plt.show()
#Labels
sns.heatmap(data=data,xticklabels=False,yticklabels=False)
plt.show()
