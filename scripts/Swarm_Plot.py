import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
df=sns.load_dataset("tips")
df.head()

sns.swarmplot(x="day",y="total_bill",data=df)
plt.show()

#hue and dodge
sns.swarmplot(x="day",y="total_bill",data=df,hue="smoker",dodge=True)
plt.show()

#Palette
sns.swarmplot(x="day",y="total_bill",data=df,hue="smoker",palette="spring")
plt.show()

#color
sns.swarmplot(x="day",y="total_bill",data=df,color="magenta")
plt.show()

#orders
sns.swarmplot(x="day",y="total_bill",data=df,order=["Sun","Thur","Fri","Sat"])
plt.show()

#Marker
sns.swarmplot(x="day",y="total_bill",data=df,marker="*",alpha=0.5)
plt.show()
#Line WIdth and edge color
sns.swarmplot(x="day",y="total_bill",data=df,linewidth=1,edgecolor="black")
plt.show()
