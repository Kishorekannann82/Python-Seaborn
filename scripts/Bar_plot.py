import numpy as np
df=sns.load_dataset("titanic")
df.head()
sns.barplot(x="who",y="fare",data=df)
plt.show()

#colors
sns.barplot(x="who",y="fare",data=df,color="magenta")
plt.show()

#hue and palette
sns.barplot(x="sex",y="fare",data=df,hue="who",palette="spring",saturation=0.2)
plt.show()

#Removing the line
sns.barplot(x="sex",y="fare",data=df,ci=False)
plt.show()

#estimator
from numpy import mean
sns.barplot(x="who",y="fare",data=df,estimator=mean)
plt.show()


#Facecolor
sns.barplot(x="who", y="fare", data=df, facecolor=(1, 1, 1, 0), edgecolor=(0.2, 0.2, 0.2))
plt.show()

#order
sns.barplot(x="who", y="fare", data=df, order=["child","man","woman"])
plt.show()
