import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df=sns.load_dataset("tips")
df.head()
#One Column
sns.stripplot(x=df["tip"],data=df)
plt.show()

#Two Column
sns.stripplot(x="day",y="tip",data=df)
plt.show()

#Hue 
sns.stripplot(x="day",y="tip",data=df,hue="sex")
plt.show()

#Palette
sns.stripplot(x="day",y="tip",data=df,hue="sex",palette="viridis")
plt.show()

#Jitter
sns.stripplot(x="day",y="tip",data=df,jitter=0.4)
plt.show()

#Dodge
sns.stripplot(x="day",y="tip",data=df,hue="sex",dodge=True)
plt.show()

#Markers and Size
sns.stripplot(x="day",y="tip",data=df,hue="sex",palette="viridis",marker="*",size=7,alpha=0.4)
plt.show()

#Line width And EdgeColor
sns.stripplot(x="day",y="tip",data=df,linewidth=2,edgecolor="pink")
plt.show()
