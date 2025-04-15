import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = sns.load_dataset("tips")

print(df.head())
sns.boxplot(x="sex",y="tip",data=df)
plt.show()
sns.boxplot(x="sex",y="tip",data=df)
plt.show()

#color
sns.boxplot(x="sex",y="tip",data=df,color="hotpink")
plt.show()

--ColorWIdth
sns.boxplot(x="sex",y="tip",data=df,linewidth=5)
plt.show()

#Gridlines and orientation
sns.set(style="whitegrid")
sns.boxplot(data=df['tip'],orient="v")
plt.show()
