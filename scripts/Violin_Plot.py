import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = sns.load_dataset("tips")

print(df.head())
sns.violinplot(x=df["total_bill"])
#Double Violin
sns.violinplot(x="sex",y="tip",data=df)
plt.show()

#Color
sns.violinplot(x="sex",y="tip",data=df,color="pink")

#Hue and Palette
sns.violinplot(x="day",y="tip",data=df,hue="sex",split=True)
plt.show()

#Split Function
sns.violinplot(x="day",y="tip",data=df,hue="sex",split=True)
plt.show()


#Saturation 
sns.violinplot(x="day",y="tip",data=df,hue="sex",split=True,saturation=0.2)
plt.show()

#order
sns.violinplot(x="sex",y="tip",data=df,color="pink",order=["Female","Male"])
plt.show()

#LineWidth
sns.violinplot(x="day",y="tip",data=df,hue="sex",split=True,saturation=0.2,linewidth=4)
plt.show()
