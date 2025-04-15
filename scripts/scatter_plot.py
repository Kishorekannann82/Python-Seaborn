import seaborn as sns
import numpy as np
import matplotlib.pyplot as pyplot
import pandas as pd
df=sns.load_dataset("exercise")
df.head()
#Hue and palette
sns.scatterplot(x="time",y="pulse",data=df,hue="kind",palette="GnBu")
plt.show()
#Marker
sns.scatterplot(x="time",y="pulse",data=df,marker="*")
plt.show()

#Transparency
sns.scatterplot(x="time",y="pulse",data=df,alpha=0.7)
plt.show()
