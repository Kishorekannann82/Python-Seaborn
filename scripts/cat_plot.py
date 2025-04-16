import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df=sns.load_dataset("tips")
df.head()

sns.catplot(x="sex",y="tip",data=df)
plt.show()
#Violin Plot
sns.catplot(x="sex",y="tip",data=df,kind="violin")
plt.show()

#Bar Plot
sns.catplot(x="sex",y="tip",data=df,kind="bar")
plt.show()
#Hue and Palette
sns.catplot(x="sex",y="tip",data=df,kind="violin",hue="smoker",palette="GnBu")
plt.show()

#Columns AND Heihght
sns.catplot(x="sex",y="tip",data=df,hue="smoker",col="time",height=2)
plt.show()

#Loadinng Titanic Dataset
df=sns.load_dataset("titanic")
df.head()

#Column Wrap
sns.catplot(x="class",col="deck",data=df[df.deck.notnull()],col_wrap=3,height=2)
plt.show()
