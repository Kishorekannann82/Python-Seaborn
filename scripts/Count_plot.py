import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = sns.load_dataset("tips")

print(df.head())


sns.countplot(x="sex",data=df)
plt.show()
#Horizontal Plot
sns.countplot(y="sex",data=df)
plt.show()
#Hue and palette
sns.countplot(x="sex",data=df,hue="smoker",palette="PuBuGn")
plt.show()
#Single Colour
sns.countplot(x="sex",data=df,color="hotpink",saturation=0.7)
plt.show()

#Face Colour
sns.countplot(x="sex",data=df,facecolor=(0,0,0,0),linewidth=7,edgecolor=sns.color_palette("GnBu",2))
